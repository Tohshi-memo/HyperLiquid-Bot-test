# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T15:52:30.833537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.0778` n `230`; crypto_major avg `-0.0557` n `8`; equity avg `-0.0284` n `100`; fx avg `-0.0096` n `6`; index avg `0.0013` n `25`; metal avg `-0.0241` n `20`; unknown avg `0.054` n `775`
- 1h: commodity avg `0.0556` n `12`; crypto_alt avg `0.3227` n `230`; crypto_major avg `0.3389` n `8`; equity avg `0.0524` n `100`; fx avg `-0.0167` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0327` n `20`; unknown avg `0.0201` n `775`
- 4h: commodity avg `0.0252` n `12`; crypto_alt avg `0.2184` n `230`; crypto_major avg `0.4474` n `8`; equity avg `0.085` n `100`; fx avg `-0.013` n `6`; index avg `0.0079` n `25`; metal avg `-0.0178` n `20`; unknown avg `-0.0419` n `775`
- 24h: commodity avg `-0.4596` n `12`; crypto_alt avg `1.2363` n `230`; crypto_major avg `1.401` n `8`; equity avg `0.8529` n `100`; fx avg `0.0053` n `6`; index avg `0.1806` n `25`; metal avg `0.1478` n `20`; unknown avg `0.1751` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
