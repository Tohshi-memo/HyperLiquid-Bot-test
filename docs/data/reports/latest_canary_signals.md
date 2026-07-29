# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T08:22:28.537173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.018` n `12`; crypto_alt avg `-0.1839` n `230`; crypto_major avg `-0.2346` n `8`; equity avg `-0.2402` n `102`; fx avg `-0.0024` n `6`; index avg `-0.0394` n `25`; metal avg `-0.0584` n `20`; unknown avg `0.0779` n `777`
- 1h: commodity avg `-0.0717` n `12`; crypto_alt avg `-0.0439` n `230`; crypto_major avg `-0.1631` n `8`; equity avg `-0.3734` n `102`; fx avg `0.0306` n `6`; index avg `-0.0268` n `25`; metal avg `-0.0944` n `20`; unknown avg `-0.068` n `777`
- 4h: commodity avg `-0.1405` n `12`; crypto_alt avg `0.575` n `230`; crypto_major avg `0.7289` n `8`; equity avg `1.7032` n `102`; fx avg `0.0539` n `6`; index avg `0.4383` n `25`; metal avg `0.1443` n `20`; unknown avg `0.0305` n `761`
- 24h: commodity avg `0.0454` n `12`; crypto_alt avg `-1.1959` n `230`; crypto_major avg `1.0156` n `8`; equity avg `-1.5948` n `102`; fx avg `-0.1061` n `6`; index avg `-0.1792` n `25`; metal avg `-0.0685` n `20`; unknown avg `-0.3284` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
