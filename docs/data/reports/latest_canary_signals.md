# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T11:52:23.997273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `0.2805` n `228`; crypto_major avg `0.2913` n `8`; equity avg `0.055` n `74`; fx avg `0.001` n `6`; index avg `0.0226` n `23`; metal avg `0.0538` n `18`; unknown avg `0.1901` n `423`
- 1h: commodity avg `0.1056` n `12`; crypto_alt avg `1.0836` n `228`; crypto_major avg `1.112` n `8`; equity avg `0.4854` n `74`; fx avg `0.0097` n `6`; index avg `0.0561` n `23`; metal avg `0.1185` n `18`; unknown avg `0.6087` n `423`
- 4h: commodity avg `0.1993` n `12`; crypto_alt avg `-0.0788` n `228`; crypto_major avg `-0.4339` n `8`; equity avg `0.4848` n `74`; fx avg `0.0077` n `6`; index avg `0.2275` n `23`; metal avg `0.0529` n `18`; unknown avg `0.2714` n `423`
- 24h: commodity avg `-1.0123` n `12`; crypto_alt avg `-3.3541` n `228`; crypto_major avg `-3.2444` n `8`; equity avg `-6.6007` n `74`; fx avg `-0.2942` n `6`; index avg `-4.0638` n `23`; metal avg `-4.5329` n `18`; unknown avg `0.2444` n `412`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
