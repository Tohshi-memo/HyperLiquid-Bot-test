# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T11:43:33.743012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0626` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0437` n `13`; crypto_alt avg `0.1723` n `239`; crypto_major avg `0.1787` n `8`; equity avg `-0.1578` n `160`; fx avg `-0.0014` n `6`; index avg `-0.0186` n `27`; metal avg `0.004` n `20`; unknown avg `3.8916` n `1258`
- 1h: commodity avg `0.2521` n `13`; crypto_alt avg `0.0213` n `239`; crypto_major avg `0.0256` n `8`; equity avg `-0.3766` n `160`; fx avg `-0.0065` n `6`; index avg `-0.0137` n `27`; metal avg `-0.0406` n `20`; unknown avg `22.7738` n `1254`
- 4h: commodity avg `0.0467` n `13`; crypto_alt avg `-0.5334` n `239`; crypto_major avg `-1.1096` n `8`; equity avg `-0.4254` n `160`; fx avg `0.0003` n `6`; index avg `-0.047` n `27`; metal avg `-0.1847` n `20`; unknown avg `1.6308` n `1219`
- 24h: commodity avg `-0.1567` n `13`; crypto_alt avg `0.3554` n `239`; crypto_major avg `-0.3672` n `8`; equity avg `3.4959` n `160`; fx avg `-0.0075` n `6`; index avg `0.3862` n `27`; metal avg `-0.1224` n `20`; unknown avg `6.6476` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2344`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
