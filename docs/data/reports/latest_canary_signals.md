# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T12:06:22.865712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1469` n `12`; crypto_alt avg `-0.4621` n `228`; crypto_major avg `-0.6186` n `8`; equity avg `-0.0629` n `74`; fx avg `0.0124` n `6`; index avg `0.0607` n `23`; metal avg `0.1132` n `18`; unknown avg `-0.0065` n `517`
- 1h: commodity avg `-0.7046` n `12`; crypto_alt avg `0.0133` n `228`; crypto_major avg `0.1306` n `8`; equity avg `0.7483` n `74`; fx avg `0.0014` n `6`; index avg `0.4648` n `23`; metal avg `0.9901` n `18`; unknown avg `0.0884` n `517`
- 4h: commodity avg `-1.0665` n `12`; crypto_alt avg `0.5297` n `228`; crypto_major avg `-0.0309` n `8`; equity avg `0.9022` n `74`; fx avg `0.0326` n `6`; index avg `0.6404` n `23`; metal avg `1.0763` n `18`; unknown avg `-0.1466` n `517`
- 24h: commodity avg `-0.244` n `12`; crypto_alt avg `0.9039` n `228`; crypto_major avg `1.7281` n `8`; equity avg `1.7938` n `74`; fx avg `-0.2626` n `6`; index avg `0.9045` n `23`; metal avg `0.2865` n `18`; unknown avg `-2.3826` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
