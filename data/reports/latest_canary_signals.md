# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T11:22:36.217335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `12`; crypto_alt avg `0.0664` n `228`; crypto_major avg `0.0913` n `8`; equity avg `0.0344` n `77`; fx avg `-0.0027` n `6`; index avg `0.0313` n `23`; metal avg `-0.0411` n `18`; unknown avg `0.1316` n `687`
- 1h: commodity avg `-0.055` n `12`; crypto_alt avg `0.081` n `228`; crypto_major avg `0.1099` n `8`; equity avg `0.1414` n `77`; fx avg `0.0025` n `6`; index avg `-0.1153` n `23`; metal avg `-0.1075` n `18`; unknown avg `0.2844` n `687`
- 4h: commodity avg `-0.4384` n `12`; crypto_alt avg `0.9739` n `228`; crypto_major avg `1.0616` n `8`; equity avg `0.5529` n `77`; fx avg `0.0571` n `6`; index avg `0.2061` n `23`; metal avg `0.6391` n `18`; unknown avg `0.5129` n `687`
- 24h: commodity avg `0.0665` n `12`; crypto_alt avg `0.1397` n `228`; crypto_major avg `2.006` n `8`; equity avg `1.7986` n `76`; fx avg `-0.0553` n `6`; index avg `0.4998` n `23`; metal avg `0.0325` n `18`; unknown avg `0.3882` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
