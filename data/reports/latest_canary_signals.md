# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T12:52:36.553099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0671` n `12`; crypto_alt avg `0.0697` n `234`; crypto_major avg `-0.088` n `8`; equity avg `0.037` n `140`; fx avg `0.0081` n `6`; index avg `0.0047` n `26`; metal avg `-0.0577` n `20`; unknown avg `0.013` n `928`
- 1h: commodity avg `0.0918` n `12`; crypto_alt avg `0.2852` n `234`; crypto_major avg `0.122` n `8`; equity avg `-0.2014` n `140`; fx avg `0.0041` n `6`; index avg `-0.0344` n `26`; metal avg `-0.1153` n `20`; unknown avg `1.2088` n `920`
- 4h: commodity avg `0.1605` n `12`; crypto_alt avg `0.2047` n `234`; crypto_major avg `0.3715` n `8`; equity avg `-0.6656` n `140`; fx avg `-0.018` n `6`; index avg `-0.1227` n `26`; metal avg `-0.1749` n `20`; unknown avg `0.8698` n `917`
- 24h: commodity avg `0.185` n `12`; crypto_alt avg `5.4412` n `234`; crypto_major avg `3.9354` n `8`; equity avg `0.6744` n `140`; fx avg `0.2429` n `6`; index avg `-0.0386` n `26`; metal avg `0.2216` n `20`; unknown avg `2.5373` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
