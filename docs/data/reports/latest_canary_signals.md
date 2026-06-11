# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T12:07:26.227314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0492` n `12`; crypto_alt avg `-0.2214` n `228`; crypto_major avg `-0.2999` n `8`; equity avg `-0.0067` n `74`; fx avg `0.0069` n `6`; index avg `0.071` n `23`; metal avg `-0.0697` n `18`; unknown avg `-0.0784` n `556`
- 1h: commodity avg `0.1648` n `12`; crypto_alt avg `0.0771` n `228`; crypto_major avg `0.0647` n `8`; equity avg `0.2465` n `74`; fx avg `0.0015` n `6`; index avg `0.1241` n `23`; metal avg `-0.1187` n `18`; unknown avg `0.2018` n `556`
- 4h: commodity avg `-0.2213` n `12`; crypto_alt avg `0.418` n `228`; crypto_major avg `0.5318` n `8`; equity avg `0.2603` n `74`; fx avg `-0.0353` n `6`; index avg `0.091` n `23`; metal avg `-0.6586` n `18`; unknown avg `0.8784` n `556`
- 24h: commodity avg `-0.6456` n `12`; crypto_alt avg `2.5215` n `228`; crypto_major avg `2.2572` n `8`; equity avg `1.6529` n `74`; fx avg `0.0324` n `6`; index avg `0.4766` n `23`; metal avg `-0.1131` n `18`; unknown avg `4.7305` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
