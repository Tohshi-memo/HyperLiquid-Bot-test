# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T21:22:26.560521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `-0.0115` n `230`; crypto_major avg `-0.0483` n `8`; equity avg `-0.0392` n `102`; fx avg `0.0181` n `6`; index avg `0.002` n `25`; metal avg `-0.008` n `20`; unknown avg `0.005` n `776`
- 1h: commodity avg `0.1195` n `12`; crypto_alt avg `-0.0564` n `230`; crypto_major avg `-0.0766` n `8`; equity avg `0.1414` n `102`; fx avg `0.0076` n `6`; index avg `0.0448` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.0396` n `776`
- 4h: commodity avg `0.0973` n `12`; crypto_alt avg `-0.037` n `230`; crypto_major avg `0.0391` n `8`; equity avg `0.5761` n `102`; fx avg `-0.0064` n `6`; index avg `-0.0284` n `25`; metal avg `-0.1092` n `20`; unknown avg `0.6719` n `774`
- 24h: commodity avg `-0.7746` n `12`; crypto_alt avg `-2.0724` n `230`; crypto_major avg `-1.5929` n `8`; equity avg `-2.8052` n `102`; fx avg `-0.0745` n `6`; index avg `-0.381` n `25`; metal avg `-0.4451` n `20`; unknown avg `1.0894` n `758`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
