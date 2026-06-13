# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T11:37:34.365266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.0415` n `228`; crypto_major avg `-0.0576` n `8`; equity avg `-0.009` n `74`; fx avg `0.0029` n `6`; index avg `-0.0066` n `23`; metal avg `-0.0606` n `18`; unknown avg `0.0034` n `644`
- 1h: commodity avg `-0.0396` n `12`; crypto_alt avg `0.3684` n `228`; crypto_major avg `0.3224` n `8`; equity avg `-0.0174` n `74`; fx avg `0.0177` n `6`; index avg `0.1248` n `23`; metal avg `-0.0318` n `18`; unknown avg `0.2962` n `644`
- 4h: commodity avg `-0.1659` n `12`; crypto_alt avg `0.4953` n `228`; crypto_major avg `0.3111` n `8`; equity avg `-0.0144` n `74`; fx avg `-0.001` n `6`; index avg `0.0892` n `23`; metal avg `-0.1227` n `18`; unknown avg `0.9475` n `635`
- 24h: commodity avg `-0.0541` n `12`; crypto_alt avg `1.2525` n `228`; crypto_major avg `0.301` n `8`; equity avg `-0.8044` n `74`; fx avg `0.023` n `6`; index avg `0.6459` n `23`; metal avg `0.3624` n `18`; unknown avg `30.5211` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
