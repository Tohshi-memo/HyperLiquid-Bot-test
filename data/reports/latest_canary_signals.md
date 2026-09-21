# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T16:38:09.409578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.6119` n `234`; crypto_major avg `-0.4475` n `8`; equity avg `-0.0984` n `140`; fx avg `0.0036` n `6`; index avg `0.0098` n `26`; metal avg `-0.0314` n `20`; unknown avg `27.9334` n `942`
- 1h: commodity avg `-0.1202` n `12`; crypto_alt avg `0.0897` n `234`; crypto_major avg `-0.1806` n `8`; equity avg `-0.0073` n `140`; fx avg `-0.0139` n `6`; index avg `0.0477` n `26`; metal avg `-0.0012` n `20`; unknown avg `26.0087` n `928`
- 4h: commodity avg `-0.3438` n `12`; crypto_alt avg `-0.5647` n `234`; crypto_major avg `0.1105` n `8`; equity avg `0.7597` n `140`; fx avg `-0.0273` n `6`; index avg `0.24` n `26`; metal avg `-0.1277` n `20`; unknown avg `32.5653` n `870`
- 24h: commodity avg `-1.1618` n `12`; crypto_alt avg `4.4044` n `234`; crypto_major avg `4.4853` n `8`; equity avg `2.5251` n `140`; fx avg `-0.0982` n `6`; index avg `0.5824` n `26`; metal avg `0.0379` n `20`; unknown avg `13.3716` n `731`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
