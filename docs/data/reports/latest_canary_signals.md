# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T07:52:35.082345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `0.0622` n `228`; crypto_major avg `0.0627` n `8`; equity avg `0.0319` n `74`; fx avg `-0.0031` n `6`; index avg `-0.0207` n `23`; metal avg `0.0203` n `18`; unknown avg `0.4747` n `643`
- 1h: commodity avg `0.0775` n `12`; crypto_alt avg `0.4836` n `228`; crypto_major avg `0.234` n `8`; equity avg `0.1683` n `74`; fx avg `-0.002` n `6`; index avg `-0.0281` n `23`; metal avg `0.082` n `18`; unknown avg `0.4703` n `643`
- 4h: commodity avg `-0.0244` n `12`; crypto_alt avg `0.8467` n `228`; crypto_major avg `0.5242` n `8`; equity avg `0.0716` n `74`; fx avg `0.0265` n `6`; index avg `-0.0489` n `23`; metal avg `0.0859` n `18`; unknown avg `-0.0327` n `619`
- 24h: commodity avg `-0.3268` n `12`; crypto_alt avg `1.9386` n `228`; crypto_major avg `1.3442` n `8`; equity avg `0.1306` n `74`; fx avg `0.0244` n `6`; index avg `1.0112` n `23`; metal avg `1.1656` n `18`; unknown avg `26.9039` n `619`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
