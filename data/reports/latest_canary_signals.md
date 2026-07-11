# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T02:22:27.407098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.0413` n `229`; crypto_major avg `0.0356` n `8`; equity avg `0.0783` n `92`; fx avg `-0.0039` n `6`; index avg `0.0049` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.0755` n `765`
- 1h: commodity avg `-0.0827` n `12`; crypto_alt avg `-0.1503` n `229`; crypto_major avg `-0.3892` n `8`; equity avg `-0.0205` n `92`; fx avg `-0.0052` n `6`; index avg `-0.0121` n `25`; metal avg `-0.005` n `20`; unknown avg `0.2218` n `765`
- 4h: commodity avg `-0.0485` n `12`; crypto_alt avg `-0.0157` n `229`; crypto_major avg `-0.1892` n `8`; equity avg `0.0842` n `92`; fx avg `0.0006` n `6`; index avg `-0.0279` n `25`; metal avg `-0.0042` n `20`; unknown avg `3.2136` n `765`
- 24h: commodity avg `-0.3805` n `12`; crypto_alt avg `0.3242` n `229`; crypto_major avg `-0.1894` n `8`; equity avg `-0.5819` n `92`; fx avg `-0.1342` n `6`; index avg `0.0921` n `25`; metal avg `0.0023` n `20`; unknown avg `4.0987` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
