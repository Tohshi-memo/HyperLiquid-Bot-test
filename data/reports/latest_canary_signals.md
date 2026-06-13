# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T12:07:36.639759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `0.1174` n `228`; crypto_major avg `0.0495` n `8`; equity avg `0.0355` n `74`; fx avg `0.0026` n `6`; index avg `0.0133` n `23`; metal avg `0.0784` n `18`; unknown avg `0.1171` n `644`
- 1h: commodity avg `-0.0391` n `12`; crypto_alt avg `0.3598` n `228`; crypto_major avg `0.3216` n `8`; equity avg `0.0366` n `74`; fx avg `-0.0028` n `6`; index avg `0.0308` n `23`; metal avg `0.1058` n `18`; unknown avg `0.3526` n `644`
- 4h: commodity avg `-0.1815` n `12`; crypto_alt avg `0.4948` n `228`; crypto_major avg `0.4199` n `8`; equity avg `-0.057` n `74`; fx avg `-0.0054` n `6`; index avg `0.1034` n `23`; metal avg `0.1747` n `18`; unknown avg `0.3848` n `635`
- 24h: commodity avg `-0.2906` n `12`; crypto_alt avg `1.0311` n `228`; crypto_major avg `0.2638` n `8`; equity avg `-0.6888` n `74`; fx avg `0.023` n `6`; index avg `0.6582` n `23`; metal avg `0.5879` n `18`; unknown avg `29.9094` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
