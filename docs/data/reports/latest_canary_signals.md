# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T12:52:29.578946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.31` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0739` n `12`; crypto_alt avg `-0.0046` n `230`; crypto_major avg `0.0442` n `8`; equity avg `0.2554` n `102`; fx avg `0.0073` n `6`; index avg `0.0351` n `25`; metal avg `0.0322` n `20`; unknown avg `0.0377` n `777`
- 1h: commodity avg `0.4008` n `12`; crypto_alt avg `-0.2739` n `230`; crypto_major avg `-0.234` n `8`; equity avg `-0.1279` n `102`; fx avg `0.0007` n `6`; index avg `-0.0899` n `25`; metal avg `-0.126` n `20`; unknown avg `0.2953` n `777`
- 4h: commodity avg `0.5613` n `12`; crypto_alt avg `-0.4505` n `230`; crypto_major avg `-0.2951` n `8`; equity avg `0.174` n `102`; fx avg `-0.0045` n `6`; index avg `-0.0218` n `25`; metal avg `-0.1936` n `20`; unknown avg `0.641` n `777`
- 24h: commodity avg `0.5295` n `12`; crypto_alt avg `-1.7673` n `230`; crypto_major avg `0.8465` n `8`; equity avg `-0.5791` n `102`; fx avg `-0.0562` n `6`; index avg `-0.1633` n `25`; metal avg `-0.1884` n `20`; unknown avg `0.0324` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
