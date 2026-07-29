# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T13:37:39.961574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.43` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.087` n `12`; crypto_alt avg `0.195` n `230`; crypto_major avg `0.0904` n `8`; equity avg `0.0559` n `102`; fx avg `0.0002` n `6`; index avg `0.0291` n `25`; metal avg `-0.0159` n `20`; unknown avg `0.366` n `777`
- 1h: commodity avg `0.1063` n `12`; crypto_alt avg `0.1909` n `230`; crypto_major avg `0.0549` n `8`; equity avg `0.0931` n `102`; fx avg `0.0005` n `6`; index avg `0.0774` n `25`; metal avg `0.0461` n `20`; unknown avg `0.4418` n `777`
- 4h: commodity avg `0.4612` n `12`; crypto_alt avg `-0.4904` n `230`; crypto_major avg `-0.4909` n `8`; equity avg `-0.4376` n `102`; fx avg `0.0007` n `6`; index avg `0.0047` n `25`; metal avg `-0.1501` n `20`; unknown avg `0.6036` n `777`
- 24h: commodity avg `0.5687` n `12`; crypto_alt avg `-1.0131` n `230`; crypto_major avg `1.38` n `8`; equity avg `0.7017` n `102`; fx avg `-0.083` n `6`; index avg `-0.0306` n `25`; metal avg `0.0117` n `20`; unknown avg `0.0995` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
