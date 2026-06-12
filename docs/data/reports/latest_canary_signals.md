# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T06:52:26.744300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1201` n `12`; crypto_alt avg `0.1969` n `228`; crypto_major avg `0.136` n `8`; equity avg `-0.1873` n `74`; fx avg `-0.0097` n `6`; index avg `-0.0934` n `23`; metal avg `-0.0036` n `18`; unknown avg `38.9923` n `557`
- 1h: commodity avg `0.2088` n `12`; crypto_alt avg `-0.6736` n `228`; crypto_major avg `-0.8591` n `8`; equity avg `-0.4347` n `74`; fx avg `0.0091` n `6`; index avg `-0.1183` n `23`; metal avg `-0.0364` n `18`; unknown avg `40.0254` n `535`
- 4h: commodity avg `-0.191` n `12`; crypto_alt avg `-1.1465` n `228`; crypto_major avg `-1.4175` n `8`; equity avg `-1.028` n `74`; fx avg `0.0042` n `6`; index avg `-0.4409` n `23`; metal avg `-0.4176` n `18`; unknown avg `41.3133` n `535`
- 24h: commodity avg `-2.0058` n `12`; crypto_alt avg `0.7229` n `228`; crypto_major avg `0.8135` n `8`; equity avg `2.4315` n `74`; fx avg `-0.0522` n `6`; index avg `1.3743` n `23`; metal avg `2.393` n `18`; unknown avg `1.5742` n `532`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
