# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T06:22:32.100448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1037` n `12`; crypto_alt avg `-0.0489` n `230`; crypto_major avg `-0.1707` n `8`; equity avg `-0.1665` n `102`; fx avg `-0.0038` n `6`; index avg `-0.0558` n `25`; metal avg `-0.0185` n `20`; unknown avg `0.0087` n `779`
- 1h: commodity avg `0.1842` n `12`; crypto_alt avg `0.1806` n `230`; crypto_major avg `0.1144` n `8`; equity avg `0.2698` n `102`; fx avg `-0.0112` n `6`; index avg `-0.0403` n `25`; metal avg `-0.0569` n `20`; unknown avg `0.0214` n `747`
- 4h: commodity avg `0.4315` n `12`; crypto_alt avg `-0.3975` n `230`; crypto_major avg `-0.6049` n `8`; equity avg `-1.0316` n `102`; fx avg `-0.091` n `6`; index avg `-0.2703` n `25`; metal avg `-0.3949` n `20`; unknown avg `0.0904` n `747`
- 24h: commodity avg `0.935` n `12`; crypto_alt avg `-0.3453` n `230`; crypto_major avg `-0.5699` n `8`; equity avg `-2.307` n `102`; fx avg `0.0147` n `6`; index avg `-0.2442` n `25`; metal avg `-0.1158` n `20`; unknown avg `-0.5622` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
