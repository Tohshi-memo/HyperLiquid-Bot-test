# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T09:52:29.184698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `12`; crypto_alt avg `0.0161` n `228`; crypto_major avg `-0.0009` n `8`; equity avg `0.0246` n `86`; fx avg `-0.0018` n `6`; index avg `0.002` n `23`; metal avg `0.0309` n `20`; unknown avg `0.0245` n `765`
- 1h: commodity avg `0.0236` n `12`; crypto_alt avg `-0.1414` n `228`; crypto_major avg `-0.1295` n `8`; equity avg `0.0612` n `86`; fx avg `0.0052` n `6`; index avg `-0.0006` n `23`; metal avg `0.0555` n `20`; unknown avg `-0.1131` n `765`
- 4h: commodity avg `0.13` n `12`; crypto_alt avg `-0.2949` n `228`; crypto_major avg `-0.1531` n `8`; equity avg `0.0752` n `86`; fx avg `0.019` n `6`; index avg `-0.0347` n `23`; metal avg `0.2171` n `20`; unknown avg `0.1171` n `733`
- 24h: commodity avg `-0.2917` n `12`; crypto_alt avg `-1.1667` n `228`; crypto_major avg `-0.8687` n `8`; equity avg `0.109` n `86`; fx avg `-0.0107` n `6`; index avg `0.4987` n `23`; metal avg `-1.2633` n `20`; unknown avg `-0.525` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
