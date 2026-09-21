# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T02:52:27.733815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `0.2856` n `234`; crypto_major avg `0.0337` n `8`; equity avg `0.0737` n `140`; fx avg `-0.0086` n `6`; index avg `0.0085` n `26`; metal avg `-0.0334` n `20`; unknown avg `-0.1277` n `944`
- 1h: commodity avg `-0.0036` n `12`; crypto_alt avg `0.1227` n `234`; crypto_major avg `0.1394` n `8`; equity avg `-0.0141` n `140`; fx avg `-0.0372` n `6`; index avg `0.006` n `26`; metal avg `-0.0749` n `20`; unknown avg `-0.4262` n `942`
- 4h: commodity avg `-0.3774` n `12`; crypto_alt avg `0.0419` n `234`; crypto_major avg `0.3391` n `8`; equity avg `0.4588` n `140`; fx avg `-0.0772` n `6`; index avg `0.0864` n `26`; metal avg `-0.003` n `20`; unknown avg `37.0933` n `935`
- 24h: commodity avg `-0.6859` n `12`; crypto_alt avg `2.3587` n `234`; crypto_major avg `2.2004` n `8`; equity avg `0.9181` n `140`; fx avg `-0.0277` n `6`; index avg `0.156` n `26`; metal avg `0.0254` n `20`; unknown avg `3.8726` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
