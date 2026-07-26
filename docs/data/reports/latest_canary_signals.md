# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T09:07:31.499545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.0383` n `230`; crypto_major avg `0.0247` n `8`; equity avg `-0.0126` n `100`; fx avg `0.0017` n `6`; index avg `-0.002` n `25`; metal avg `0.0169` n `20`; unknown avg `0.0036` n `775`
- 1h: commodity avg `-0.031` n `12`; crypto_alt avg `-0.0309` n `230`; crypto_major avg `0.1162` n `8`; equity avg `-0.033` n `100`; fx avg `-0.005` n `6`; index avg `0.0023` n `25`; metal avg `0.0221` n `20`; unknown avg `-0.0464` n `775`
- 4h: commodity avg `-0.0417` n `12`; crypto_alt avg `0.3873` n `230`; crypto_major avg `0.0054` n `8`; equity avg `-0.0496` n `100`; fx avg `-0.0456` n `6`; index avg `-0.0063` n `25`; metal avg `0.0381` n `20`; unknown avg `-0.0287` n `759`
- 24h: commodity avg `-0.6391` n `12`; crypto_alt avg `1.8352` n `230`; crypto_major avg `1.9301` n `8`; equity avg `0.5475` n `100`; fx avg `-0.0092` n `6`; index avg `0.1394` n `25`; metal avg `0.0975` n `20`; unknown avg `0.0451` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1852`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1439`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1289`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1281`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.123`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1207`, n `666`, weak_sample_signal
