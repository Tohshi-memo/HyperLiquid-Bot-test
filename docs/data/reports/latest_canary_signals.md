# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T15:52:17.437575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0726` n `12`; crypto_alt avg `-0.0277` n `228`; crypto_major avg `-0.0142` n `8`; equity avg `0.0335` n `65`; fx avg `0.0009` n `5`; index avg `0.0` n `23`; metal avg `0.0032` n `18`; unknown avg `-0.0075` n `384`
- 1h: commodity avg `0.1085` n `12`; crypto_alt avg `-0.0233` n `228`; crypto_major avg `0.0429` n `8`; equity avg `0.0548` n `65`; fx avg `0.0` n `5`; index avg `0.0494` n `23`; metal avg `0.0489` n `18`; unknown avg `-0.0613` n `384`
- 4h: commodity avg `0.0482` n `12`; crypto_alt avg `-0.3484` n `228`; crypto_major avg `-0.2619` n `8`; equity avg `0.0326` n `65`; fx avg `0.0028` n `5`; index avg `0.0532` n `23`; metal avg `0.0222` n `18`; unknown avg `-0.093` n `383`
- 24h: commodity avg `1.8094` n `12`; crypto_alt avg `-9.2984` n `228`; crypto_major avg `-2.5134` n `8`; equity avg `-2.5693` n `65`; fx avg `-0.1649` n `5`; index avg `-1.5968` n `23`; metal avg `-5.8277` n `18`; unknown avg `550.0068` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
