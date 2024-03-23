import { sortByDate } from "@lib/utils/sortFunctions";
import Link from "next/link";

const InnerPagination = ({ posts, date }) => {
  const orderedPosts = sortByDate(posts);
  const lastIndex = orderedPosts.length - 1;
  const postIndex = orderedPosts.findIndex(
    (post) => post.frontmatter.date == date
  );
  const next = postIndex == 0 ? undefined : orderedPosts[postIndex - 1].slug;
  const prev =
    postIndex == lastIndex ? undefined : orderedPosts[postIndex + 1].slug;
  const prevButton = prev && (
    <Link href={prev} className="btn btn-outline-primary" style={{ minWidth: '100px', whiteSpace: 'nowrap', margin: '0 2px' }}>
    ＜ 前のページ 
    </Link>
  );
  const nextButton = next && (
    <Link href={next} className={"btn btn-primary"}　style={{ minWidth: '100px', whiteSpace: 'nowrap', margin: '0 2px'}}>
      次のページ ＞
    </Link>
  );

  return (
  <div style={{ display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap'  }}>
    <span>{prevButton}</span>
    <span>{nextButton}</span>
  </div>
  );
};

export default InnerPagination;
