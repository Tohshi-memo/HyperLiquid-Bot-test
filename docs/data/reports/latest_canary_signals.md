# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T21:37:26.579449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.6046` n `228`; crypto_major avg `0.8158` n `8`; equity avg `0.019` n `86`; fx avg `-0.0088` n `6`; index avg `-0.0106` n `23`; metal avg `0.0394` n `20`; unknown avg `0.6097` n `765`
- 1h: commodity avg `-0.0676` n `12`; crypto_alt avg `0.7175` n `228`; crypto_major avg `0.7271` n `8`; equity avg `-0.0672` n `86`; fx avg `-0.0193` n `6`; index avg `-0.0292` n `23`; metal avg `0.0249` n `20`; unknown avg `1.0925` n `765`
- 4h: commodity avg `-0.0708` n `12`; crypto_alt avg `0.4758` n `228`; crypto_major avg `0.4136` n `8`; equity avg `0.132` n `86`; fx avg `-0.0042` n `6`; index avg `-0.0043` n `23`; metal avg `-0.0972` n `20`; unknown avg `0.7845` n `765`
- 24h: commodity avg `0.3444` n `12`; crypto_alt avg `-0.8383` n `228`; crypto_major avg `-1.0111` n `8`; equity avg `-1.9483` n `86`; fx avg `0.0851` n `6`; index avg `-0.1662` n `23`; metal avg `0.3274` n `20`; unknown avg `1.0781` n `700`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
