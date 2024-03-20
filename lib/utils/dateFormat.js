import { formatInTimeZone } from "date-fns-tz";

const dateFormat = (date) => {
  return formatInTimeZone(date, "Asia/Tokyo", "yyyy年M月d日");
};

export default dateFormat;

export function addYears(date, years) {
  return new Date(date).setFullYear(new Date(date).getFullYear() + years);
}
