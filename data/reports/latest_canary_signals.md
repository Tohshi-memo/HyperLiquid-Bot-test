# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T10:45:27.859371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.0216` n `230`; crypto_major avg `-0.0566` n `8`; equity avg `-0.0083` n `121`; fx avg `-0.0025` n `6`; index avg `-0.0011` n `25`; metal avg `0.0092` n `20`; unknown avg `0.0824` n `795`
- 1h: commodity avg `0.012` n `12`; crypto_alt avg `0.5939` n `230`; crypto_major avg `0.3189` n `8`; equity avg `0.0362` n `121`; fx avg `-0.0039` n `6`; index avg `0.0114` n `25`; metal avg `0.0228` n `20`; unknown avg `0.2284` n `794`
- 4h: commodity avg `-0.0215` n `12`; crypto_alt avg `2.5728` n `230`; crypto_major avg `1.4646` n `8`; equity avg `0.2563` n `121`; fx avg `0.0173` n `6`; index avg `0.0399` n `25`; metal avg `0.0072` n `20`; unknown avg `0.5446` n `794`
- 24h: commodity avg `-0.0043` n `12`; crypto_alt avg `0.0016` n `230`; crypto_major avg `0.8129` n `8`; equity avg `0.3331` n `121`; fx avg `0.042` n `6`; index avg `0.0458` n `25`; metal avg `0.0474` n `20`; unknown avg `2.936` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
