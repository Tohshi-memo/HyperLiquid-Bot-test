# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T00:07:29.298907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `0.1136` n `230`; crypto_major avg `0.0289` n `8`; equity avg `0.2318` n `102`; fx avg `0.0127` n `6`; index avg `0.0446` n `25`; metal avg `-0.022` n `20`; unknown avg `-0.0225` n `781`
- 1h: commodity avg `-0.0052` n `12`; crypto_alt avg `0.2342` n `230`; crypto_major avg `-0.011` n `8`; equity avg `0.1856` n `102`; fx avg `-0.0149` n `6`; index avg `0.0277` n `25`; metal avg `-0.0271` n `20`; unknown avg `4.7265` n `781`
- 4h: commodity avg `0.6024` n `12`; crypto_alt avg `0.1375` n `230`; crypto_major avg `0.043` n `8`; equity avg `-0.1811` n `102`; fx avg `-0.0924` n `6`; index avg `-0.0457` n `25`; metal avg `-0.0431` n `20`; unknown avg `2.6106` n `780`
- 24h: commodity avg `0.7942` n `12`; crypto_alt avg `-0.4425` n `230`; crypto_major avg `-2.2362` n `8`; equity avg `-1.8122` n `102`; fx avg `-0.0299` n `6`; index avg `-0.1142` n `25`; metal avg `-0.4338` n `20`; unknown avg `2.7209` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
