# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T03:37:29.333596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.4949` n `230`; crypto_major avg `-0.2204` n `8`; equity avg `-0.3821` n `102`; fx avg `-0.0032` n `6`; index avg `-0.0429` n `25`; metal avg `-0.0282` n `20`; unknown avg `-0.0467` n `777`
- 1h: commodity avg `0.062` n `12`; crypto_alt avg `-0.9178` n `230`; crypto_major avg `-0.5351` n `8`; equity avg `-0.8544` n `102`; fx avg `0.0043` n `6`; index avg `-0.1152` n `25`; metal avg `-0.1204` n `20`; unknown avg `0.1862` n `777`
- 4h: commodity avg `-0.0244` n `12`; crypto_alt avg `-1.26` n `230`; crypto_major avg `-0.0955` n `8`; equity avg `-1.2868` n `102`; fx avg `-0.0084` n `6`; index avg `-0.4333` n `25`; metal avg `0.0202` n `20`; unknown avg `1.5913` n `777`
- 24h: commodity avg `-0.0884` n `12`; crypto_alt avg `-1.3175` n `230`; crypto_major avg `0.2062` n `8`; equity avg `-2.7758` n `102`; fx avg `-0.0964` n `6`; index avg `-0.4946` n `25`; metal avg `-0.1679` n `20`; unknown avg `0.4239` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
