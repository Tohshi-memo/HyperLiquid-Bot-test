# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T10:52:29.791186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0235` n `12`; crypto_alt avg `-0.0496` n `230`; crypto_major avg `-0.0506` n `8`; equity avg `-0.0834` n `100`; fx avg `0.0044` n `6`; index avg `-0.016` n `25`; metal avg `-0.0234` n `20`; unknown avg `-0.0965` n `773`
- 1h: commodity avg `0.2026` n `12`; crypto_alt avg `-0.4071` n `230`; crypto_major avg `-0.2356` n `8`; equity avg `-0.2558` n `100`; fx avg `0.0017` n `6`; index avg `-0.0358` n `25`; metal avg `-0.0298` n `20`; unknown avg `-0.1289` n `773`
- 4h: commodity avg `-0.1193` n `12`; crypto_alt avg `-0.4682` n `230`; crypto_major avg `-0.2538` n `8`; equity avg `0.5224` n `100`; fx avg `-0.0503` n `6`; index avg `0.1285` n `25`; metal avg `0.2628` n `20`; unknown avg `0.0536` n `772`
- 24h: commodity avg `-0.1271` n `12`; crypto_alt avg `-1.3401` n `230`; crypto_major avg `-1.7548` n `8`; equity avg `-1.9015` n `99`; fx avg `-0.1354` n `6`; index avg `-0.4916` n `25`; metal avg `-0.3534` n `20`; unknown avg `0.1685` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0887`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.083`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
