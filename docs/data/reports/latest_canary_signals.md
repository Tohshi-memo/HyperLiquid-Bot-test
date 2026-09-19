# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T17:07:26.476016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.228` n `234`; crypto_major avg `0.2853` n `8`; equity avg `0.0368` n `140`; fx avg `-0.0006` n `6`; index avg `-0.003` n `26`; metal avg `0.0001` n `20`; unknown avg `17.3125` n `911`
- 1h: commodity avg `0.0136` n `12`; crypto_alt avg `0.6697` n `234`; crypto_major avg `0.4343` n `8`; equity avg `0.0559` n `140`; fx avg `-0.004` n `6`; index avg `0.0096` n `26`; metal avg `-0.0019` n `20`; unknown avg `16.8193` n `903`
- 4h: commodity avg `-0.1394` n `12`; crypto_alt avg `0.6535` n `234`; crypto_major avg `0.5079` n `8`; equity avg `0.0824` n `140`; fx avg `-0.0081` n `6`; index avg `0.0143` n `26`; metal avg `0.0017` n `20`; unknown avg `5.2173` n `884`
- 24h: commodity avg `-0.083` n `12`; crypto_alt avg `3.3496` n `234`; crypto_major avg `1.95` n `8`; equity avg `0.6754` n `140`; fx avg `0.0305` n `6`; index avg `0.1462` n `26`; metal avg `-0.0932` n `20`; unknown avg `3.6709` n `774`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
