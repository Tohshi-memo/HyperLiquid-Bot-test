# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T16:37:24.323395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.65` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8029` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0379` n `12`; crypto_alt avg `-0.1282` n `230`; crypto_major avg `-0.2481` n `8`; equity avg `0.1748` n `102`; fx avg `0.0037` n `6`; index avg `0.0188` n `25`; metal avg `0.0448` n `20`; unknown avg `-0.0092` n `778`
- 1h: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.2102` n `230`; crypto_major avg `-0.2917` n `8`; equity avg `-0.415` n `102`; fx avg `-0.0301` n `6`; index avg `-0.0795` n `25`; metal avg `0.0269` n `20`; unknown avg `-0.0826` n `778`
- 4h: commodity avg `0.2035` n `12`; crypto_alt avg `-0.4531` n `230`; crypto_major avg `-0.5529` n `8`; equity avg `-2.3558` n `102`; fx avg `-0.0444` n `6`; index avg `-0.2921` n `25`; metal avg `0.0097` n `20`; unknown avg `0.2957` n `777`
- 24h: commodity avg `1.462` n `12`; crypto_alt avg `-2.5562` n `230`; crypto_major avg `-0.6525` n `8`; equity avg `-2.371` n `102`; fx avg `-0.0963` n `6`; index avg `-0.5688` n `25`; metal avg `-0.3349` n `20`; unknown avg `-0.0328` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
