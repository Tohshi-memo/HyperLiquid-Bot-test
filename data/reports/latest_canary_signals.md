# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T02:07:33.615521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `13`; crypto_alt avg `-0.0368` n `237`; crypto_major avg `-0.0294` n `8`; equity avg `0.0124` n `152`; fx avg `-0.0006` n `6`; index avg `0.0027` n `26`; metal avg `0.0005` n `20`; unknown avg `0.7464` n `1228`
- 1h: commodity avg `-0.0783` n `13`; crypto_alt avg `0.3314` n `237`; crypto_major avg `0.2804` n `8`; equity avg `0.088` n `152`; fx avg `0.0018` n `6`; index avg `0.0075` n `26`; metal avg `0.0073` n `20`; unknown avg `0.2328` n `1230`
- 4h: commodity avg `-0.0913` n `13`; crypto_alt avg `-0.8779` n `237`; crypto_major avg `-0.697` n `8`; equity avg `-0.0937` n `152`; fx avg `-0.0101` n `6`; index avg `-0.0267` n `26`; metal avg `-0.045` n `20`; unknown avg `4.241` n `1218`
- 24h: commodity avg `0.2414` n `13`; crypto_alt avg `-1.0005` n `237`; crypto_major avg `-0.4998` n `8`; equity avg `0.9087` n `152`; fx avg `-0.0369` n `6`; index avg `0.1141` n `26`; metal avg `-0.0212` n `20`; unknown avg `205.1242` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
