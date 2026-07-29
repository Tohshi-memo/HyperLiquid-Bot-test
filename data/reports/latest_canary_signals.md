# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T00:37:38.586818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1313` n `12`; crypto_alt avg `-0.1871` n `230`; crypto_major avg `-0.0581` n `8`; equity avg `-0.5855` n `102`; fx avg `-0.0128` n `6`; index avg `-0.0916` n `25`; metal avg `0.0216` n `20`; unknown avg `0.0007` n `777`
- 1h: commodity avg `-0.0544` n `12`; crypto_alt avg `0.2577` n `230`; crypto_major avg `0.492` n `8`; equity avg `1.0363` n `102`; fx avg `0.0227` n `6`; index avg `0.1414` n `25`; metal avg `0.1007` n `20`; unknown avg `0.1631` n `777`
- 4h: commodity avg `0.6738` n `12`; crypto_alt avg `0.0818` n `230`; crypto_major avg `0.183` n `8`; equity avg `0.5143` n `102`; fx avg `0.0201` n `6`; index avg `0.1202` n `25`; metal avg `0.0515` n `20`; unknown avg `-0.0474` n `776`
- 24h: commodity avg `-0.1718` n `12`; crypto_alt avg `-0.1012` n `230`; crypto_major avg `0.4004` n `8`; equity avg `-1.4578` n `102`; fx avg `-0.1245` n `6`; index avg `-0.0692` n `25`; metal avg `-0.2526` n `20`; unknown avg `0.3915` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
