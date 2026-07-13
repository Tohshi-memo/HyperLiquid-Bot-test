# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T05:07:26.319196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3049` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0332` n `12`; crypto_alt avg `0.1046` n `230`; crypto_major avg `0.1034` n `8`; equity avg `0.1351` n `92`; fx avg `-0.0232` n `6`; index avg `0.0332` n `25`; metal avg `0.0727` n `20`; unknown avg `-0.0211` n `766`
- 1h: commodity avg `0.0672` n `12`; crypto_alt avg `0.4524` n `230`; crypto_major avg `0.1345` n `8`; equity avg `0.1061` n `92`; fx avg `-0.0218` n `6`; index avg `-0.0011` n `25`; metal avg `0.084` n `20`; unknown avg `0.0013` n `766`
- 4h: commodity avg `0.0528` n `12`; crypto_alt avg `-1.1717` n `230`; crypto_major avg `-1.576` n `8`; equity avg `-1.2575` n `92`; fx avg `0.0256` n `6`; index avg `-0.2711` n `25`; metal avg `-0.1496` n `20`; unknown avg `4.1303` n `766`
- 24h: commodity avg `0.169` n `12`; crypto_alt avg `-1.885` n `230`; crypto_major avg `-1.265` n `8`; equity avg `-2.3137` n `92`; fx avg `0.0249` n `6`; index avg `-0.5073` n `25`; metal avg `-0.4255` n `20`; unknown avg `-0.1017` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
