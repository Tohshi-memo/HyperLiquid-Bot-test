# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T11:52:39.290195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.09` n `12`; crypto_alt avg `0.1157` n `228`; crypto_major avg `0.0947` n `8`; equity avg `-0.0462` n `77`; fx avg `-0.0124` n `6`; index avg `0.026` n `23`; metal avg `0.1509` n `18`; unknown avg `-0.0954` n `687`
- 1h: commodity avg `0.0055` n `12`; crypto_alt avg `-0.4231` n `228`; crypto_major avg `-0.3589` n `8`; equity avg `-0.1059` n `77`; fx avg `-0.0094` n `6`; index avg `0.0648` n `23`; metal avg `-0.0184` n `18`; unknown avg `0.0842` n `687`
- 4h: commodity avg `-0.2626` n `12`; crypto_alt avg `0.3051` n `228`; crypto_major avg `0.558` n `8`; equity avg `0.3322` n `77`; fx avg `0.0396` n `6`; index avg `0.188` n `23`; metal avg `0.6229` n `18`; unknown avg `0.3562` n `687`
- 24h: commodity avg `0.0183` n `12`; crypto_alt avg `-0.1684` n `228`; crypto_major avg `1.4674` n `8`; equity avg `1.557` n `76`; fx avg `-0.0768` n `6`; index avg `0.4788` n `23`; metal avg `0.0571` n `18`; unknown avg `0.5162` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
