# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T11:37:30.953662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0921` n `12`; crypto_alt avg `-0.1084` n `230`; crypto_major avg `-0.2067` n `8`; equity avg `-0.1891` n `102`; fx avg `0.0074` n `6`; index avg `-0.0903` n `25`; metal avg `0.0097` n `20`; unknown avg `-0.0423` n `777`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `-0.2722` n `230`; crypto_major avg `-0.2774` n `8`; equity avg `-0.0933` n `102`; fx avg `0.016` n `6`; index avg `0.0159` n `25`; metal avg `0.0095` n `20`; unknown avg `0.0074` n `777`
- 4h: commodity avg `0.1506` n `12`; crypto_alt avg `-0.2495` n `230`; crypto_major avg `-0.3311` n `8`; equity avg `0.1948` n `102`; fx avg `0.0403` n `6`; index avg `0.0464` n `25`; metal avg `-0.1991` n `20`; unknown avg `-0.2513` n `777`
- 24h: commodity avg `0.077` n `12`; crypto_alt avg `-1.335` n `230`; crypto_major avg `1.0983` n `8`; equity avg `-0.2104` n `102`; fx avg `-0.0505` n `6`; index avg `0.0242` n `25`; metal avg `0.0546` n `20`; unknown avg `-0.4393` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
