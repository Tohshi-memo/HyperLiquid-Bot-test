# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T22:22:33.241125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `0.1293` n `234`; crypto_major avg `0.1678` n `8`; equity avg `0.0181` n `140`; fx avg `-0.0051` n `6`; index avg `-0.0011` n `26`; metal avg `0.0039` n `20`; unknown avg `0.1872` n `944`
- 1h: commodity avg `-0.0317` n `12`; crypto_alt avg `0.1482` n `234`; crypto_major avg `0.6579` n `8`; equity avg `0.1107` n `140`; fx avg `-0.0072` n `6`; index avg `0.0225` n `26`; metal avg `0.0517` n `20`; unknown avg `-0.2324` n `942`
- 4h: commodity avg `-0.1158` n `12`; crypto_alt avg `0.6396` n `234`; crypto_major avg `1.2162` n `8`; equity avg `0.077` n `140`; fx avg `-0.0111` n `6`; index avg `0.0085` n `26`; metal avg `0.0341` n `20`; unknown avg `-0.3275` n `852`
- 24h: commodity avg `-0.8227` n `12`; crypto_alt avg `3.6255` n `234`; crypto_major avg `6.4334` n `8`; equity avg `2.7381` n `140`; fx avg `-0.1392` n `6`; index avg `0.5706` n `26`; metal avg `0.0258` n `20`; unknown avg `7.7299` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
