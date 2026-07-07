# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T08:22:27.542783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `0.1604` n `229`; crypto_major avg `0.2469` n `8`; equity avg `0.1102` n `91`; fx avg `-0.0143` n `6`; index avg `0.018` n `25`; metal avg `0.0904` n `20`; unknown avg `-0.0174` n `763`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `-0.228` n `229`; crypto_major avg `-0.3414` n `8`; equity avg `-0.1114` n `91`; fx avg `-0.0366` n `6`; index avg `-0.0175` n `25`; metal avg `0.1223` n `20`; unknown avg `-0.1937` n `763`
- 4h: commodity avg `0.2357` n `12`; crypto_alt avg `0.1711` n `229`; crypto_major avg `0.3662` n `8`; equity avg `0.5552` n `91`; fx avg `-0.024` n `6`; index avg `0.0782` n `25`; metal avg `0.1014` n `20`; unknown avg `12.1934` n `745`
- 24h: commodity avg `0.5223` n `12`; crypto_alt avg `0.4524` n `229`; crypto_major avg `-0.3332` n `8`; equity avg `-1.321` n `90`; fx avg `-0.0674` n `6`; index avg `-0.3464` n `25`; metal avg `-0.344` n `20`; unknown avg `-0.3838` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
