# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T15:37:29.425940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.025` n `12`; crypto_alt avg `-0.1056` n `228`; crypto_major avg `-0.0855` n `8`; equity avg `0.0328` n `74`; fx avg `-0.0026` n `6`; index avg `0.035` n `23`; metal avg `0.004` n `18`; unknown avg `-0.0071` n `644`
- 1h: commodity avg `-0.0234` n `12`; crypto_alt avg `0.6621` n `228`; crypto_major avg `0.2433` n `8`; equity avg `0.1929` n `74`; fx avg `0.0009` n `6`; index avg `0.0699` n `23`; metal avg `0.0768` n `18`; unknown avg `-1.9109` n `644`
- 4h: commodity avg `-0.0874` n `12`; crypto_alt avg `0.6646` n `228`; crypto_major avg `0.9156` n `8`; equity avg `0.3821` n `74`; fx avg `-0.014` n `6`; index avg `0.2127` n `23`; metal avg `0.2759` n `18`; unknown avg `-1.8959` n `644`
- 24h: commodity avg `-0.5643` n `12`; crypto_alt avg `1.6855` n `228`; crypto_major avg `0.3553` n `8`; equity avg `0.1478` n `74`; fx avg `0.0109` n `6`; index avg `0.5675` n `23`; metal avg `0.4426` n `18`; unknown avg `-1.7311` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
