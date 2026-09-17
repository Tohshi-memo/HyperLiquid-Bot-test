# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T17:07:36.865172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `12`; crypto_alt avg `0.4189` n `234`; crypto_major avg `0.4409` n `8`; equity avg `0.0485` n `138`; fx avg `0.0077` n `6`; index avg `0.0057` n `26`; metal avg `0.0607` n `20`; unknown avg `0.3505` n `917`
- 1h: commodity avg `0.2349` n `12`; crypto_alt avg `0.5143` n `234`; crypto_major avg `0.2952` n `8`; equity avg `0.2659` n `138`; fx avg `0.0326` n `6`; index avg `0.0366` n `26`; metal avg `0.0187` n `20`; unknown avg `0.4792` n `911`
- 4h: commodity avg `0.4292` n `12`; crypto_alt avg `1.2584` n `234`; crypto_major avg `0.6341` n `8`; equity avg `0.3293` n `138`; fx avg `-0.0008` n `6`; index avg `0.0299` n `26`; metal avg `0.0641` n `20`; unknown avg `1.6336` n `891`
- 24h: commodity avg `-0.0005` n `12`; crypto_alt avg `5.4616` n `234`; crypto_major avg `3.0192` n `8`; equity avg `2.0733` n `138`; fx avg `0.0595` n `6`; index avg `0.3007` n `26`; metal avg `0.2967` n `20`; unknown avg `0.6389` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
