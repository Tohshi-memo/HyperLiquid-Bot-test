# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T15:53:03.766312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1497` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2046` n `12`; crypto_alt avg `-0.0461` n `231`; crypto_major avg `-0.025` n `8`; equity avg `-0.1217` n `122`; fx avg `0.0065` n `6`; index avg `0.0053` n `25`; metal avg `-0.1091` n `20`; unknown avg `0.0292` n `797`
- 1h: commodity avg `0.2046` n `12`; crypto_alt avg `-0.0461` n `231`; crypto_major avg `-0.025` n `8`; equity avg `-0.1217` n `122`; fx avg `0.0065` n `6`; index avg `0.0053` n `25`; metal avg `-0.1091` n `20`; unknown avg `0.0292` n `797`
- 4h: commodity avg `0.4866` n `12`; crypto_alt avg `-1.3474` n `231`; crypto_major avg `-1.1449` n `8`; equity avg `-0.3186` n `122`; fx avg `-0.02` n `6`; index avg `0.0048` n `25`; metal avg `-0.2587` n `20`; unknown avg `-0.2029` n `797`
- 24h: commodity avg `0.4554` n `12`; crypto_alt avg `-2.1411` n `231`; crypto_major avg `-2.1831` n `8`; equity avg `-0.4698` n `122`; fx avg `-0.0474` n `6`; index avg `0.0351` n `25`; metal avg `-0.3005` n `20`; unknown avg `0.2759` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1576`, n `671`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `671`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1066`, n `671`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `671`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `671`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `671`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `671`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0848`, n `671`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `671`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0714`, n `671`, weak_sample_signal
