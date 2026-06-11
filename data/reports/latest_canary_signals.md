# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T11:52:28.333580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.142` n `12`; crypto_alt avg `0.3394` n `228`; crypto_major avg `0.2814` n `8`; equity avg `0.0152` n `74`; fx avg `-0.0074` n `6`; index avg `0.0072` n `23`; metal avg `0.0315` n `18`; unknown avg `0.0032` n `556`
- 1h: commodity avg `0.071` n `12`; crypto_alt avg `0.4499` n `228`; crypto_major avg `0.5481` n `8`; equity avg `0.1047` n `74`; fx avg `0.0084` n `6`; index avg `-0.061` n `23`; metal avg `-0.0948` n `18`; unknown avg `0.4747` n `556`
- 4h: commodity avg `-0.3131` n `12`; crypto_alt avg `0.8601` n `228`; crypto_major avg `1.0305` n `8`; equity avg `0.5116` n `74`; fx avg `-0.0617` n `6`; index avg `0.236` n `23`; metal avg `-0.4138` n `18`; unknown avg `1.2126` n `556`
- 24h: commodity avg `-0.7871` n `12`; crypto_alt avg `2.671` n `228`; crypto_major avg `2.4079` n `8`; equity avg `1.6571` n `74`; fx avg `0.0246` n `6`; index avg `0.3793` n `23`; metal avg `-0.4573` n `18`; unknown avg `5.468` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
