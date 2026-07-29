# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T12:37:36.152738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0553` n `12`; crypto_alt avg `-0.0766` n `230`; crypto_major avg `-0.018` n `8`; equity avg `0.0083` n `102`; fx avg `0.0022` n `6`; index avg `0.006` n `25`; metal avg `0.062` n `20`; unknown avg `-0.0038` n `777`
- 1h: commodity avg `0.2716` n `12`; crypto_alt avg `-0.2241` n `230`; crypto_major avg `-0.1295` n `8`; equity avg `-0.3577` n `102`; fx avg `-0.011` n `6`; index avg `-0.1149` n `25`; metal avg `-0.1465` n `20`; unknown avg `0.5633` n `777`
- 4h: commodity avg `0.4269` n `12`; crypto_alt avg `-0.3821` n `230`; crypto_major avg `-0.2461` n `8`; equity avg `0.0923` n `102`; fx avg `0.0008` n `6`; index avg `0.0284` n `25`; metal avg `-0.2153` n `20`; unknown avg `0.567` n `777`
- 24h: commodity avg `0.419` n `12`; crypto_alt avg `-1.6392` n `230`; crypto_major avg `0.979` n `8`; equity avg `-0.7326` n `102`; fx avg `-0.0704` n `6`; index avg `-0.1876` n `25`; metal avg `-0.1585` n `20`; unknown avg `0.0526` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
