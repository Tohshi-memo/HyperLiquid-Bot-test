# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T13:07:22.350123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0521` n `12`; crypto_alt avg `-0.1416` n `230`; crypto_major avg `-0.1627` n `8`; equity avg `-0.0278` n `100`; fx avg `0.0` n `6`; index avg `0.0013` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.0448` n `775`
- 1h: commodity avg `0.0349` n `12`; crypto_alt avg `-0.2463` n `230`; crypto_major avg `-0.3253` n `8`; equity avg `-0.0628` n `100`; fx avg `0.003` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.0243` n `775`
- 4h: commodity avg `-0.241` n `12`; crypto_alt avg `-0.1707` n `230`; crypto_major avg `-0.1669` n `8`; equity avg `0.1969` n `100`; fx avg `0.0096` n `6`; index avg `0.0481` n `25`; metal avg `0.0875` n `20`; unknown avg `-0.106` n `775`
- 24h: commodity avg `-0.7801` n `12`; crypto_alt avg `1.1577` n `230`; crypto_major avg `1.2389` n `8`; equity avg `0.7027` n `100`; fx avg `0.0255` n `6`; index avg `0.1663` n `25`; metal avg `0.1827` n `20`; unknown avg `0.0363` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
