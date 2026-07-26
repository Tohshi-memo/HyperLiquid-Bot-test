# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T16:22:23.338392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `0.0565` n `230`; crypto_major avg `0.114` n `8`; equity avg `0.0145` n `100`; fx avg `-0.0186` n `6`; index avg `0.0086` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0064` n `775`
- 1h: commodity avg `0.0122` n `12`; crypto_alt avg `0.2349` n `230`; crypto_major avg `0.1231` n `8`; equity avg `-0.0222` n `100`; fx avg `-0.0155` n `6`; index avg `0.0069` n `25`; metal avg `0.0059` n `20`; unknown avg `0.0129` n `775`
- 4h: commodity avg `0.0343` n `12`; crypto_alt avg `0.3009` n `230`; crypto_major avg `0.462` n `8`; equity avg `0.1371` n `100`; fx avg `-0.0224` n `6`; index avg `0.038` n `25`; metal avg `0.02` n `20`; unknown avg `0.0491` n `775`
- 24h: commodity avg `-0.4768` n `12`; crypto_alt avg `1.3451` n `230`; crypto_major avg `1.4763` n `8`; equity avg `0.8898` n `100`; fx avg `0.006` n `6`; index avg `0.1949` n `25`; metal avg `0.1874` n `20`; unknown avg `0.1829` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
