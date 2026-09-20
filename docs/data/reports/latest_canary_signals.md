# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T01:38:00.179200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.4125` n `234`; crypto_major avg `-0.3442` n `8`; equity avg `-0.0196` n `140`; fx avg `-0.0133` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.5859` n `943`
- 1h: commodity avg `0.0458` n `12`; crypto_alt avg `-0.7231` n `234`; crypto_major avg `-0.5342` n `8`; equity avg `-0.0144` n `140`; fx avg `0.0011` n `6`; index avg `0.0092` n `26`; metal avg `0.0049` n `20`; unknown avg `0.0403` n `941`
- 4h: commodity avg `0.1036` n `12`; crypto_alt avg `0.6214` n `234`; crypto_major avg `-0.1027` n `8`; equity avg `0.0303` n `140`; fx avg `-0.003` n `6`; index avg `-0.021` n `26`; metal avg `0.0101` n `20`; unknown avg `0.5681` n `911`
- 24h: commodity avg `0.0344` n `12`; crypto_alt avg `1.1415` n `234`; crypto_major avg `-0.5755` n `8`; equity avg `0.1005` n `140`; fx avg `-0.0717` n `6`; index avg `0.0107` n `26`; metal avg `0.0346` n `20`; unknown avg `0.3774` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
