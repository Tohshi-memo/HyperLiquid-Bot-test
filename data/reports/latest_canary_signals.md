# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T20:22:29.264501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `-0.0334` n `228`; crypto_major avg `0.0697` n `8`; equity avg `0.0066` n `74`; fx avg `-0.0079` n `6`; index avg `0.0119` n `23`; metal avg `0.0025` n `18`; unknown avg `0.1009` n `644`
- 1h: commodity avg `0.1158` n `12`; crypto_alt avg `0.0293` n `228`; crypto_major avg `0.0711` n `8`; equity avg `0.0619` n `74`; fx avg `-0.0106` n `6`; index avg `0.0795` n `23`; metal avg `0.0176` n `18`; unknown avg `0.2773` n `644`
- 4h: commodity avg `-0.0594` n `12`; crypto_alt avg `-0.0992` n `228`; crypto_major avg `0.0355` n `8`; equity avg `0.1075` n `74`; fx avg `0.0207` n `6`; index avg `-0.0058` n `23`; metal avg `0.0839` n `18`; unknown avg `-0.2141` n `644`
- 24h: commodity avg `-0.7101` n `12`; crypto_alt avg `1.7931` n `228`; crypto_major avg `0.505` n `8`; equity avg `0.4603` n `74`; fx avg `0.056` n `6`; index avg `0.5734` n `23`; metal avg `0.2403` n `18`; unknown avg `-1.5684` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
