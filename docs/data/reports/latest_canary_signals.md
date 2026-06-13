# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T10:37:27.257487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `0.0013` n `228`; crypto_major avg `0.0568` n `8`; equity avg `0.0346` n `74`; fx avg `-0.0205` n `6`; index avg `-0.0003` n `23`; metal avg `-0.073` n `18`; unknown avg `-0.0931` n `644`
- 1h: commodity avg `-0.1851` n `12`; crypto_alt avg `-0.0705` n `228`; crypto_major avg `-0.0315` n `8`; equity avg `0.0841` n `74`; fx avg `0.0036` n `6`; index avg `-0.0441` n `23`; metal avg `-0.0796` n `18`; unknown avg `-0.0134` n `643`
- 4h: commodity avg `-0.1605` n `12`; crypto_alt avg `0.8471` n `228`; crypto_major avg `0.3896` n `8`; equity avg `0.1952` n `74`; fx avg `-0.0171` n `6`; index avg `-0.0243` n `23`; metal avg `-0.0229` n `18`; unknown avg `0.3274` n `635`
- 24h: commodity avg `-0.0813` n `12`; crypto_alt avg `0.656` n `228`; crypto_major avg `0.0919` n `8`; equity avg `-0.621` n `74`; fx avg `-0.017` n `6`; index avg `0.6387` n `23`; metal avg `0.1759` n `18`; unknown avg `30.6518` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
