# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T11:07:27.806769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.018` n `13`; crypto_alt avg `0.0717` n `237`; crypto_major avg `0.1012` n `8`; equity avg `0.0017` n `152`; fx avg `0.0117` n `6`; index avg `0.0036` n `26`; metal avg `0.0048` n `20`; unknown avg `1.2649` n `1229`
- 1h: commodity avg `0.0456` n `13`; crypto_alt avg `-0.2805` n `237`; crypto_major avg `-0.0253` n `8`; equity avg `0.0108` n `152`; fx avg `0.0075` n `6`; index avg `-0.0111` n `26`; metal avg `0.0128` n `20`; unknown avg `1.6018` n `1227`
- 4h: commodity avg `-0.0654` n `13`; crypto_alt avg `-0.8532` n `237`; crypto_major avg `-0.5119` n `8`; equity avg `-0.0766` n `152`; fx avg `0.0253` n `6`; index avg `-0.0022` n `26`; metal avg `0.0087` n `20`; unknown avg `20.8046` n `1181`
- 24h: commodity avg `0.0299` n `13`; crypto_alt avg `-1.955` n `237`; crypto_major avg `-0.2691` n `8`; equity avg `-0.0308` n `152`; fx avg `-0.0069` n `6`; index avg `0.0163` n `26`; metal avg `-0.0395` n `20`; unknown avg `21.7703` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1977`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
