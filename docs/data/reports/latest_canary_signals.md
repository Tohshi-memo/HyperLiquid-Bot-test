# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T06:37:30.366625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.2206` n `230`; crypto_major avg `0.4135` n `8`; equity avg `0.4396` n `102`; fx avg `-0.0052` n `6`; index avg `0.1011` n `25`; metal avg `0.0632` n `20`; unknown avg `-0.0577` n `777`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `0.2298` n `230`; crypto_major avg `0.4766` n `8`; equity avg `0.183` n `102`; fx avg `0.012` n `6`; index avg `0.0892` n `25`; metal avg `0.069` n `20`; unknown avg `-0.0796` n `761`
- 4h: commodity avg `-0.006` n `12`; crypto_alt avg `-0.7162` n `230`; crypto_major avg `0.4018` n `8`; equity avg `0.0728` n `102`; fx avg `-0.0676` n `6`; index avg `0.0707` n `25`; metal avg `0.0251` n `20`; unknown avg `-0.0965` n `761`
- 24h: commodity avg `-0.0361` n `12`; crypto_alt avg `-1.2937` n `230`; crypto_major avg `1.1477` n `8`; equity avg `-1.3673` n `102`; fx avg `-0.1497` n `6`; index avg `-0.2368` n `25`; metal avg `0.0313` n `20`; unknown avg `-0.2807` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
