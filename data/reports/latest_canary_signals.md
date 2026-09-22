# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T14:22:32.941991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `12`; crypto_alt avg `-0.1613` n `234`; crypto_major avg `-0.2356` n `8`; equity avg `0.004` n `140`; fx avg `-0.0031` n `6`; index avg `0.0056` n `26`; metal avg `0.0398` n `20`; unknown avg `-0.106` n `942`
- 1h: commodity avg `0.3469` n `12`; crypto_alt avg `-0.2953` n `234`; crypto_major avg `0.1089` n `8`; equity avg `1.1501` n `140`; fx avg `-0.0579` n `6`; index avg `0.1383` n `26`; metal avg `-0.0754` n `20`; unknown avg `1.4293` n `898`
- 4h: commodity avg `0.4045` n `12`; crypto_alt avg `0.8042` n `234`; crypto_major avg `0.6183` n `8`; equity avg `0.8898` n `140`; fx avg `-0.0106` n `6`; index avg `0.1339` n `26`; metal avg `0.161` n `20`; unknown avg `1.4898` n `892`
- 24h: commodity avg `0.02` n `12`; crypto_alt avg `1.1952` n `234`; crypto_major avg `1.7464` n `8`; equity avg `1.5566` n `140`; fx avg `-0.2774` n `6`; index avg `0.3` n `26`; metal avg `-0.0126` n `20`; unknown avg `9050.5339` n `806`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
