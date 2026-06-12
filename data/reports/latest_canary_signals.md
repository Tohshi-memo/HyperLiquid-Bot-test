# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T17:37:41.201459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0916` n `12`; crypto_alt avg `0.1449` n `228`; crypto_major avg `0.2651` n `8`; equity avg `-0.1044` n `74`; fx avg `0.0089` n `6`; index avg `-0.0686` n `23`; metal avg `-0.0118` n `18`; unknown avg `-0.0118` n `643`
- 1h: commodity avg `-0.1684` n `12`; crypto_alt avg `0.057` n `228`; crypto_major avg `0.1869` n `8`; equity avg `0.2671` n `74`; fx avg `0.0057` n `6`; index avg `0.1403` n `23`; metal avg `0.0867` n `18`; unknown avg `-0.1229` n `643`
- 4h: commodity avg `-0.2898` n `12`; crypto_alt avg `0.3184` n `228`; crypto_major avg `1.0823` n `8`; equity avg `0.803` n `74`; fx avg `-0.0105` n `6`; index avg `0.5965` n `23`; metal avg `0.4457` n `18`; unknown avg `26.6788` n `643`
- 24h: commodity avg `-0.7024` n `12`; crypto_alt avg `0.6207` n `228`; crypto_major avg `1.832` n `8`; equity avg `1.5317` n `74`; fx avg `-0.0069` n `6`; index avg `1.3508` n `23`; metal avg `1.3586` n `18`; unknown avg `43.1881` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
