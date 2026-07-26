# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T03:07:28.671022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `12`; crypto_alt avg `-0.0023` n `230`; crypto_major avg `-0.0539` n `8`; equity avg `0.0018` n `100`; fx avg `-0.0032` n `6`; index avg `0.0033` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0237` n `774`
- 1h: commodity avg `-0.0507` n `12`; crypto_alt avg `0.1948` n `230`; crypto_major avg `0.1322` n `8`; equity avg `0.0448` n `100`; fx avg `-0.005` n `6`; index avg `0.0023` n `25`; metal avg `-0.0033` n `20`; unknown avg `-0.1067` n `774`
- 4h: commodity avg `0.0129` n `12`; crypto_alt avg `0.1924` n `230`; crypto_major avg `0.2396` n `8`; equity avg `0.1905` n `100`; fx avg `0.018` n `6`; index avg `0.041` n `25`; metal avg `0.0152` n `20`; unknown avg `-0.3077` n `774`
- 24h: commodity avg `-0.4624` n `12`; crypto_alt avg `0.7274` n `230`; crypto_major avg `1.2251` n `8`; equity avg `0.4107` n `100`; fx avg `-0.0066` n `6`; index avg `0.1338` n `25`; metal avg `0.0331` n `20`; unknown avg `-0.2467` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1377`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1234`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1213`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1185`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1179`, n `666`, weak_sample_signal
