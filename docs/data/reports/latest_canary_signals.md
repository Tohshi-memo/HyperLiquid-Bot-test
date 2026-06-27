# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T14:07:25.843207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `-0.013` n `228`; crypto_major avg `0.0454` n `8`; equity avg `0.0013` n `88`; fx avg `0.0006` n `6`; index avg `0.0208` n `23`; metal avg `-0.0011` n `20`; unknown avg `-0.0046` n `764`
- 1h: commodity avg `0.0512` n `12`; crypto_alt avg `0.2365` n `228`; crypto_major avg `0.2986` n `8`; equity avg `0.0713` n `88`; fx avg `-0.0006` n `6`; index avg `0.0068` n `23`; metal avg `0.003` n `20`; unknown avg `0.0327` n `764`
- 4h: commodity avg `0.1279` n `12`; crypto_alt avg `0.4192` n `228`; crypto_major avg `0.5404` n `8`; equity avg `0.1372` n `88`; fx avg `0.0211` n `6`; index avg `0.0019` n `23`; metal avg `0.0104` n `20`; unknown avg `0.2469` n `764`
- 24h: commodity avg `0.3534` n `12`; crypto_alt avg `1.5561` n `228`; crypto_major avg `1.3738` n `8`; equity avg `0.9325` n `87`; fx avg `0.0199` n `6`; index avg `-0.0484` n `23`; metal avg `0.0604` n `20`; unknown avg `0.3329` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2075`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
