# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T13:22:25.554654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1659` n `12`; crypto_alt avg `-0.6461` n `228`; crypto_major avg `-0.8335` n `8`; equity avg `0.0666` n `73`; fx avg `0.0019` n `6`; index avg `-0.034` n `23`; metal avg `-0.0192` n `18`; unknown avg `-0.29` n `425`
- 1h: commodity avg `0.1958` n `12`; crypto_alt avg `0.8409` n `228`; crypto_major avg `0.2113` n `8`; equity avg `0.5536` n `73`; fx avg `0.0086` n `6`; index avg `0.0942` n `23`; metal avg `0.2029` n `18`; unknown avg `0.783` n `423`
- 4h: commodity avg `-0.1757` n `12`; crypto_alt avg `0.7262` n `228`; crypto_major avg `0.3541` n `8`; equity avg `0.7872` n `73`; fx avg `0.0308` n `6`; index avg `0.0031` n `23`; metal avg `1.0226` n `18`; unknown avg `-0.022` n `422`
- 24h: commodity avg `-0.27` n `12`; crypto_alt avg `-7.2902` n `228`; crypto_major avg `-5.9771` n `8`; equity avg `-4.083` n `73`; fx avg `0.1324` n `6`; index avg `-1.484` n `23`; metal avg `0.2321` n `18`; unknown avg `-1.314` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
