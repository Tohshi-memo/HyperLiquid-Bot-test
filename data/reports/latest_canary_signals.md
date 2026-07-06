# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T06:07:31.153706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1163` n `12`; crypto_alt avg `-0.0153` n `229`; crypto_major avg `-0.0707` n `8`; equity avg `0.0273` n `88`; fx avg `-0.0011` n `6`; index avg `0.022` n `25`; metal avg `-0.0493` n `20`; unknown avg `-0.0162` n `733`
- 1h: commodity avg `0.2076` n `12`; crypto_alt avg `-0.4168` n `229`; crypto_major avg `-0.364` n `8`; equity avg `-0.051` n `88`; fx avg `0.0012` n `6`; index avg `-0.003` n `25`; metal avg `-0.0348` n `20`; unknown avg `-0.2699` n `733`
- 4h: commodity avg `0.1175` n `12`; crypto_alt avg `-0.9295` n `229`; crypto_major avg `-0.8387` n `8`; equity avg `0.1386` n `88`; fx avg `-0.016` n `6`; index avg `0.0264` n `25`; metal avg `-0.2893` n `20`; unknown avg `-0.1547` n `733`
- 24h: commodity avg `0.0144` n `12`; crypto_alt avg `0.0416` n `229`; crypto_major avg `0.9778` n `8`; equity avg `-0.6574` n `88`; fx avg `0.0674` n `6`; index avg `-0.0394` n `25`; metal avg `-0.295` n `20`; unknown avg `0.987` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
