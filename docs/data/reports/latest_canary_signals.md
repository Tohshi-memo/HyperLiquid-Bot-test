# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T16:22:34.479813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0615` n `12`; crypto_alt avg `0.0523` n `234`; crypto_major avg `0.0585` n `8`; equity avg `0.1105` n `138`; fx avg `0.011` n `6`; index avg `0.0117` n `26`; metal avg `-0.0058` n `20`; unknown avg `0.1846` n `919`
- 1h: commodity avg `0.0035` n `12`; crypto_alt avg `0.9164` n `234`; crypto_major avg `0.6108` n `8`; equity avg `0.3793` n `138`; fx avg `-0.0127` n `6`; index avg `0.0432` n `26`; metal avg `0.0485` n `20`; unknown avg `0.6421` n `915`
- 4h: commodity avg `0.3037` n `12`; crypto_alt avg `0.5512` n `234`; crypto_major avg `0.3131` n `8`; equity avg `0.4413` n `138`; fx avg `-0.0039` n `6`; index avg `0.0493` n `26`; metal avg `-0.0312` n `20`; unknown avg `0.9689` n `891`
- 24h: commodity avg `-0.1846` n `12`; crypto_alt avg `5.0239` n `234`; crypto_major avg `2.7141` n `8`; equity avg `1.8478` n `138`; fx avg `0.0163` n `6`; index avg `0.2511` n `26`; metal avg `0.2114` n `20`; unknown avg `0.8729` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
