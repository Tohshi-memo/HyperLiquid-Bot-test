# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T02:07:26.367153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2064` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0356` n `13`; crypto_alt avg `0.0746` n `239`; crypto_major avg `-0.0253` n `8`; equity avg `-0.1009` n `168`; fx avg `0.0076` n `6`; index avg `-0.0175` n `27`; metal avg `0.0073` n `20`; unknown avg `0.1975` n `1255`
- 1h: commodity avg `-0.1334` n `13`; crypto_alt avg `-0.1735` n `239`; crypto_major avg `-0.6711` n `8`; equity avg `-0.0449` n `168`; fx avg `-0.0128` n `6`; index avg `-0.0222` n `27`; metal avg `0.2315` n `20`; unknown avg `1.8461` n `1259`
- 4h: commodity avg `-0.1117` n `13`; crypto_alt avg `-0.5515` n `239`; crypto_major avg `-1.3571` n `8`; equity avg `-1.1435` n `168`; fx avg `0.0232` n `6`; index avg `-0.1507` n `27`; metal avg `0.0242` n `20`; unknown avg `1.1041` n `1173`
- 24h: commodity avg `0.5254` n `13`; crypto_alt avg `-3.6507` n `239`; crypto_major avg `-3.6165` n `8`; equity avg `-4.8323` n `167`; fx avg `0.1653` n `6`; index avg `-0.4758` n `27`; metal avg `-1.0168` n `20`; unknown avg `636.4011` n `1029`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
