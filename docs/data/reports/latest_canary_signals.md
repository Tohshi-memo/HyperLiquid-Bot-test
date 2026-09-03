# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T12:37:27.814230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0495` n `12`; crypto_alt avg `0.2614` n `232`; crypto_major avg `0.422` n `8`; equity avg `0.3638` n `133`; fx avg `0.0082` n `6`; index avg `0.0753` n `26`; metal avg `0.206` n `20`; unknown avg `13.2112` n `792`
- 1h: commodity avg `-0.0449` n `12`; crypto_alt avg `0.218` n `232`; crypto_major avg `0.3451` n `8`; equity avg `0.2603` n `133`; fx avg `-0.0472` n `6`; index avg `0.0544` n `26`; metal avg `0.2146` n `20`; unknown avg `0.7556` n `790`
- 4h: commodity avg `0.2983` n `12`; crypto_alt avg `0.336` n `232`; crypto_major avg `0.5165` n `8`; equity avg `-0.0358` n `133`; fx avg `-0.112` n `6`; index avg `-0.0069` n `26`; metal avg `0.1553` n `20`; unknown avg `2.3789` n `790`
- 24h: commodity avg `0.6508` n `12`; crypto_alt avg `2.325` n `232`; crypto_major avg `2.4339` n `8`; equity avg `1.3601` n `133`; fx avg `-0.4206` n `6`; index avg `0.1065` n `26`; metal avg `0.8163` n `20`; unknown avg `0.0487` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0431`, n `668`, weak_sample_signal
