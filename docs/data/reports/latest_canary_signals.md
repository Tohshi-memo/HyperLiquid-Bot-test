# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T05:07:33.977101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `0.0025` n `230`; crypto_major avg `0.0261` n `8`; equity avg `-0.0286` n `100`; fx avg `-0.0015` n `6`; index avg `0.0073` n `25`; metal avg `-0.0003` n `20`; unknown avg `1.4436` n `774`
- 1h: commodity avg `0.0402` n `12`; crypto_alt avg `0.0831` n `230`; crypto_major avg `0.0701` n `8`; equity avg `-0.0025` n `100`; fx avg `-0.0023` n `6`; index avg `0.0266` n `25`; metal avg `0.005` n `20`; unknown avg `0.383` n `774`
- 4h: commodity avg `-0.1125` n `12`; crypto_alt avg `-0.1059` n `230`; crypto_major avg `0.0451` n `8`; equity avg `0.1724` n `100`; fx avg `-0.0439` n `6`; index avg `0.0425` n `25`; metal avg `-0.0179` n `20`; unknown avg `-0.1939` n `774`
- 24h: commodity avg `-0.4254` n `12`; crypto_alt avg `-1.1779` n `230`; crypto_major avg `-0.9636` n `8`; equity avg `-2.5005` n `100`; fx avg `-0.0668` n `6`; index avg `-0.1714` n `25`; metal avg `0.1677` n `20`; unknown avg `13.7038` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1144`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1043`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1027`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1007`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
