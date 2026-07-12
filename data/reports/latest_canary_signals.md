# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T15:37:24.947246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.04` n `230`; crypto_major avg `-0.0222` n `8`; equity avg `-0.023` n `92`; fx avg `-0.0022` n `6`; index avg `0.0025` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.0077` n `765`
- 1h: commodity avg `-0.0237` n `12`; crypto_alt avg `0.2632` n `230`; crypto_major avg `0.2958` n `8`; equity avg `0.0103` n `92`; fx avg `-0.0034` n `6`; index avg `0.0157` n `25`; metal avg `0.0098` n `20`; unknown avg `0.0279` n `765`
- 4h: commodity avg `-0.0898` n `12`; crypto_alt avg `0.2293` n `230`; crypto_major avg `0.4833` n `8`; equity avg `0.0144` n `92`; fx avg `0.0075` n `6`; index avg `0.0366` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.0834` n `765`
- 24h: commodity avg `0.4329` n `12`; crypto_alt avg `-0.8977` n `230`; crypto_major avg `-0.4166` n `8`; equity avg `0.0001` n `92`; fx avg `0.0229` n `6`; index avg `-0.1036` n `25`; metal avg `-0.0838` n `20`; unknown avg `0.1211` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
