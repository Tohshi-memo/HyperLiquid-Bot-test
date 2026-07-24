# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T13:37:28.998569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.048` n `12`; crypto_alt avg `-0.1426` n `230`; crypto_major avg `-0.2209` n `8`; equity avg `-0.6497` n `100`; fx avg `0.0005` n `6`; index avg `-0.0612` n `25`; metal avg `0.0455` n `20`; unknown avg `-0.1158` n `773`
- 1h: commodity avg `0.1185` n `12`; crypto_alt avg `-0.9002` n `230`; crypto_major avg `-0.7576` n `8`; equity avg `-1.0215` n `100`; fx avg `0.0085` n `6`; index avg `-0.1358` n `25`; metal avg `-0.1375` n `20`; unknown avg `-0.1504` n `773`
- 4h: commodity avg `0.3423` n `12`; crypto_alt avg `-1.2466` n `230`; crypto_major avg `-1.0177` n `8`; equity avg `-0.9921` n `100`; fx avg `-0.0284` n `6`; index avg `-0.1221` n `25`; metal avg `-0.0866` n `20`; unknown avg `-0.2616` n `773`
- 24h: commodity avg `-0.1022` n `12`; crypto_alt avg `-1.8796` n `230`; crypto_major avg `-1.7342` n `8`; equity avg `-1.6924` n `100`; fx avg `-0.1462` n `6`; index avg `-0.355` n `25`; metal avg `-0.1775` n `20`; unknown avg `0.1001` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1038`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0976`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
