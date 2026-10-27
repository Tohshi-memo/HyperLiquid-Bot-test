# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T01:07:31.089405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0477` n `13`; crypto_alt avg `0.0532` n `237`; crypto_major avg `0.0242` n `8`; equity avg `-0.042` n `154`; fx avg `-0.0105` n `6`; index avg `-0.0023` n `27`; metal avg `-0.0396` n `20`; unknown avg `-0.0829` n `1234`
- 1h: commodity avg `-0.0522` n `13`; crypto_alt avg `-0.1332` n `237`; crypto_major avg `0.0966` n `8`; equity avg `-0.0158` n `154`; fx avg `-0.0089` n `6`; index avg `0.0044` n `27`; metal avg `-0.0812` n `20`; unknown avg `0.1331` n `1234`
- 4h: commodity avg `-0.0855` n `13`; crypto_alt avg `0.7656` n `237`; crypto_major avg `0.9218` n `8`; equity avg `0.663` n `154`; fx avg `-0.0147` n `6`; index avg `0.1579` n `27`; metal avg `-0.0703` n `20`; unknown avg `-0.1937` n `1208`
- 24h: commodity avg `-0.0439` n `13`; crypto_alt avg `0.5022` n `237`; crypto_major avg `0.9129` n `8`; equity avg `2.0948` n `153`; fx avg `-0.0262` n `6`; index avg `0.1842` n `27`; metal avg `0.045` n `20`; unknown avg `1000.634` n `1002`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2267`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
