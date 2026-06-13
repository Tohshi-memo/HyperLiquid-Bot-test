# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T11:22:31.120849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.3729` n `228`; crypto_major avg `0.3335` n `8`; equity avg `0.043` n `74`; fx avg `-0.0043` n `6`; index avg `0.0227` n `23`; metal avg `-0.1446` n `18`; unknown avg `0.2646` n `644`
- 1h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.4117` n `228`; crypto_major avg `0.4374` n `8`; equity avg `0.0262` n `74`; fx avg `-0.0057` n `6`; index avg `0.1306` n `23`; metal avg `-0.0431` n `18`; unknown avg `0.1462` n `644`
- 4h: commodity avg `-0.0983` n `12`; crypto_alt avg `0.8799` n `228`; crypto_major avg `0.6047` n `8`; equity avg `0.0733` n `74`; fx avg `-0.0038` n `6`; index avg `0.0679` n `23`; metal avg `-0.0506` n `18`; unknown avg `0.8761` n `635`
- 24h: commodity avg `0.2334` n `12`; crypto_alt avg `1.051` n `228`; crypto_major avg `0.2256` n `8`; equity avg `-0.7993` n `74`; fx avg `0.0086` n `6`; index avg `0.6286` n `23`; metal avg `0.2766` n `18`; unknown avg `30.5395` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
