# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T06:07:26.464201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `0.3241` n `228`; crypto_major avg `0.129` n `8`; equity avg `0.0113` n `74`; fx avg `0.003` n `6`; index avg `-0.0088` n `23`; metal avg `-0.0073` n `18`; unknown avg `-0.3143` n `629`
- 1h: commodity avg `0.0098` n `12`; crypto_alt avg `0.5157` n `228`; crypto_major avg `0.1297` n `8`; equity avg `-0.0001` n `74`; fx avg `0.0029` n `6`; index avg `-0.0082` n `23`; metal avg `0.0068` n `18`; unknown avg `0.025` n `629`
- 4h: commodity avg `-0.0338` n `12`; crypto_alt avg `-0.1204` n `228`; crypto_major avg `-0.2417` n `8`; equity avg `-0.1141` n `74`; fx avg `-0.0063` n `6`; index avg `-0.0507` n `23`; metal avg `0.029` n `18`; unknown avg `-0.8358` n `613`
- 24h: commodity avg `-0.6116` n `12`; crypto_alt avg `1.8528` n `228`; crypto_major avg `1.7254` n `8`; equity avg `0.8013` n `74`; fx avg `-0.027` n `6`; index avg `0.2523` n `23`; metal avg `0.3239` n `18`; unknown avg `-1.1163` n `603`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
