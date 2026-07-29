# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T11:52:26.839644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.25` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0534` n `12`; crypto_alt avg `0.044` n `230`; crypto_major avg `0.1489` n `8`; equity avg `0.0246` n `102`; fx avg `-0.0044` n `6`; index avg `0.0099` n `25`; metal avg `0.0115` n `20`; unknown avg `0.1505` n `777`
- 1h: commodity avg `-0.1686` n `12`; crypto_alt avg `0.0553` n `230`; crypto_major avg `0.0606` n `8`; equity avg `0.1953` n `102`; fx avg `0.0063` n `6`; index avg `0.0523` n `25`; metal avg `0.0711` n `20`; unknown avg `0.2244` n `777`
- 4h: commodity avg `0.0849` n `12`; crypto_alt avg `-0.1991` n `230`; crypto_major avg `-0.2221` n `8`; equity avg `0.3539` n `102`; fx avg `0.0286` n `6`; index avg `0.0894` n `25`; metal avg `-0.1551` n `20`; unknown avg `-0.2429` n `777`
- 24h: commodity avg `0.0075` n `12`; crypto_alt avg `-1.2778` n `230`; crypto_major avg `1.2941` n `8`; equity avg `-0.2242` n `102`; fx avg `-0.0464` n `6`; index avg `0.0097` n `25`; metal avg `0.1192` n `20`; unknown avg `-0.3026` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
