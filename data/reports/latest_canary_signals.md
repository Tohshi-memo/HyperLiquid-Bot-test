# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T20:37:26.136042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.0121` n `230`; crypto_major avg `-0.0078` n `8`; equity avg `-0.0098` n `100`; fx avg `0.003` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0145` n `20`; unknown avg `-0.0114` n `775`
- 1h: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.0833` n `230`; crypto_major avg `-0.0441` n `8`; equity avg `-0.0375` n `100`; fx avg `0.0049` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0398` n `20`; unknown avg `0.0083` n `775`
- 4h: commodity avg `0.2127` n `12`; crypto_alt avg `-0.4326` n `230`; crypto_major avg `-0.4194` n `8`; equity avg `-0.1036` n `100`; fx avg `0.0381` n `6`; index avg `-0.0433` n `25`; metal avg `-0.0199` n `20`; unknown avg `-0.1997` n `775`
- 24h: commodity avg `-0.1797` n `12`; crypto_alt avg `0.7886` n `230`; crypto_major avg `0.828` n `8`; equity avg `0.5845` n `100`; fx avg `0.0478` n `6`; index avg `0.0848` n `25`; metal avg `0.1741` n `20`; unknown avg `-0.0765` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1923`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1828`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
