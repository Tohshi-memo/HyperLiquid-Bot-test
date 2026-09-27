# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T10:22:30.046648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `0.0926` n `234`; crypto_major avg `0.057` n `8`; equity avg `-0.0052` n `141`; fx avg `-0.0018` n `6`; index avg `0.0006` n `26`; metal avg `-0.0003` n `20`; unknown avg `-0.0861` n `962`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `0.3579` n `234`; crypto_major avg `0.3551` n `8`; equity avg `0.0318` n `141`; fx avg `-0.0121` n `6`; index avg `0.0059` n `26`; metal avg `0.0082` n `20`; unknown avg `0.0275` n `959`
- 4h: commodity avg `-0.0177` n `12`; crypto_alt avg `0.8324` n `234`; crypto_major avg `0.7775` n `8`; equity avg `0.1558` n `141`; fx avg `-0.0213` n `6`; index avg `0.0322` n `26`; metal avg `0.0152` n `20`; unknown avg `1.7784` n `943`
- 24h: commodity avg `0.0648` n `12`; crypto_alt avg `1.0624` n `234`; crypto_major avg `0.908` n `8`; equity avg `0.4026` n `141`; fx avg `-0.0173` n `6`; index avg `0.0432` n `26`; metal avg `0.0048` n `20`; unknown avg `5.5581` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
