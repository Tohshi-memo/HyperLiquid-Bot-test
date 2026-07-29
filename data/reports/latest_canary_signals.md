# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T10:15:59.586491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.0234` n `230`; crypto_major avg `-0.0248` n `8`; equity avg `-0.0856` n `102`; fx avg `0.0034` n `6`; index avg `-0.0029` n `25`; metal avg `-0.0207` n `20`; unknown avg `-0.005` n `777`
- 1h: commodity avg `0.1516` n `12`; crypto_alt avg `-0.0045` n `230`; crypto_major avg `0.0713` n `8`; equity avg `0.1349` n `102`; fx avg `-0.0209` n `6`; index avg `0.0541` n `25`; metal avg `-0.0862` n `20`; unknown avg `0.0227` n `777`
- 4h: commodity avg `0.091` n `12`; crypto_alt avg `0.2233` n `230`; crypto_major avg `0.3361` n `8`; equity avg `1.4378` n `102`; fx avg `0.0358` n `6`; index avg `0.3256` n `25`; metal avg `-0.1024` n `20`; unknown avg `-0.1775` n `777`
- 24h: commodity avg `0.104` n `12`; crypto_alt avg `-1.1355` n `230`; crypto_major avg `1.3432` n `8`; equity avg `-0.4262` n `102`; fx avg `-0.0589` n `6`; index avg `-0.0099` n `25`; metal avg `0.0809` n `20`; unknown avg `-0.5249` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
