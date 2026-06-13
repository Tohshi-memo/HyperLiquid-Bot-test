# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T13:07:32.724370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1191` n `12`; crypto_alt avg `-0.1365` n `228`; crypto_major avg `0.0091` n `8`; equity avg `0.0212` n `74`; fx avg `0.0` n `6`; index avg `0.0391` n `23`; metal avg `-0.2826` n `18`; unknown avg `0.9855` n `644`
- 1h: commodity avg `-0.0996` n `12`; crypto_alt avg `0.0233` n `228`; crypto_major avg `0.4081` n `8`; equity avg `0.1465` n `74`; fx avg `-0.0014` n `6`; index avg `0.1279` n `23`; metal avg `-0.2287` n `18`; unknown avg `1.1651` n `644`
- 4h: commodity avg `-0.5465` n `12`; crypto_alt avg `0.4517` n `228`; crypto_major avg `0.6372` n `8`; equity avg `0.0637` n `74`; fx avg `0.1216` n `6`; index avg `0.1638` n `23`; metal avg `-0.0283` n `18`; unknown avg `1.685` n `635`
- 24h: commodity avg `-0.7299` n `12`; crypto_alt avg `1.118` n `228`; crypto_major avg `0.5986` n `8`; equity avg `0.0965` n `74`; fx avg `0.0312` n `6`; index avg `1.0341` n `23`; metal avg `0.7419` n `18`; unknown avg `27.1129` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
