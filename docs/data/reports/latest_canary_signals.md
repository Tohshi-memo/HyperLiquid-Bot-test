# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T18:37:38.377166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0325` n `12`; crypto_alt avg `0.0171` n `230`; crypto_major avg `0.0815` n `8`; equity avg `0.0107` n `102`; fx avg `0.0059` n `6`; index avg `-0.001` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0031` n `775`
- 1h: commodity avg `-0.005` n `12`; crypto_alt avg `0.1453` n `230`; crypto_major avg `0.2849` n `8`; equity avg `-0.275` n `102`; fx avg `-0.0179` n `6`; index avg `-0.0598` n `25`; metal avg `-0.0646` n `20`; unknown avg `-0.1755` n `774`
- 4h: commodity avg `-0.3531` n `12`; crypto_alt avg `0.3636` n `230`; crypto_major avg `0.8026` n `8`; equity avg `1.0631` n `102`; fx avg `-0.0186` n `6`; index avg `0.0976` n `25`; metal avg `0.0753` n `20`; unknown avg `-0.1998` n `774`
- 24h: commodity avg `-0.9899` n `12`; crypto_alt avg `-1.8964` n `230`; crypto_major avg `-1.5878` n `8`; equity avg `-2.7324` n `102`; fx avg `-0.113` n `6`; index avg `-0.2712` n `25`; metal avg `-0.3744` n `20`; unknown avg `-0.4583` n `758`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
