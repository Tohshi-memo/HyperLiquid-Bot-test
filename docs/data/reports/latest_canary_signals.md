# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T13:22:29.609767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `0.0177` n `230`; crypto_major avg `0.1254` n `8`; equity avg `0.0688` n `100`; fx avg `0.0` n `6`; index avg `0.0055` n `25`; metal avg `0.0029` n `20`; unknown avg `0.0069` n `775`
- 1h: commodity avg `0.0738` n `12`; crypto_alt avg `-0.1206` n `230`; crypto_major avg `-0.0907` n `8`; equity avg `0.0243` n `100`; fx avg `-0.0001` n `6`; index avg `0.0116` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.1052` n `775`
- 4h: commodity avg `-0.1625` n `12`; crypto_alt avg `-0.0917` n `230`; crypto_major avg `-0.0905` n `8`; equity avg `0.2175` n `100`; fx avg `0.0091` n `6`; index avg `0.0475` n `25`; metal avg `0.0708` n `20`; unknown avg `-0.0996` n `775`
- 24h: commodity avg `-0.7849` n `12`; crypto_alt avg `1.1846` n `230`; crypto_major avg `1.353` n `8`; equity avg `0.7902` n `100`; fx avg `0.0207` n `6`; index avg `0.1786` n `25`; metal avg `0.1891` n `20`; unknown avg `0.0406` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
