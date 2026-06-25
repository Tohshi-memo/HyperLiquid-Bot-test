# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T22:52:35.334110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.1759` n `228`; crypto_major avg `-0.1282` n `8`; equity avg `0.0678` n `86`; fx avg `-0.0005` n `6`; index avg `0.0106` n `23`; metal avg `-0.098` n `20`; unknown avg `0.1531` n `765`
- 1h: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.2315` n `228`; crypto_major avg `-0.1989` n `8`; equity avg `-0.2442` n `86`; fx avg `-0.0161` n `6`; index avg `-0.034` n `23`; metal avg `-0.1057` n `20`; unknown avg `-0.6153` n `765`
- 4h: commodity avg `-0.1171` n `12`; crypto_alt avg `0.6894` n `228`; crypto_major avg `0.5705` n `8`; equity avg `-0.2434` n `86`; fx avg `-0.0231` n `6`; index avg `-0.0424` n `23`; metal avg `-0.2011` n `20`; unknown avg `0.5417` n `765`
- 24h: commodity avg `0.3873` n `12`; crypto_alt avg `-1.2242` n `228`; crypto_major avg `-1.21` n `8`; equity avg `-2.4827` n `86`; fx avg `0.1031` n `6`; index avg `-0.2383` n `23`; metal avg `0.2429` n `20`; unknown avg `0.9468` n `700`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
