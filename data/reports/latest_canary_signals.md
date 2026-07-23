# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T01:07:27.151052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `-0.0767` n `230`; crypto_major avg `-0.0673` n `8`; equity avg `0.0488` n `98`; fx avg `-0.0145` n `6`; index avg `0.0163` n `25`; metal avg `0.0203` n `20`; unknown avg `-0.056` n `773`
- 1h: commodity avg `0.0124` n `12`; crypto_alt avg `0.0906` n `230`; crypto_major avg `-0.0649` n `8`; equity avg `0.258` n `98`; fx avg `-0.0593` n `6`; index avg `0.0806` n `25`; metal avg `0.0286` n `20`; unknown avg `-0.15` n `773`
- 4h: commodity avg `0.2751` n `12`; crypto_alt avg `-0.0526` n `230`; crypto_major avg `0.2644` n `8`; equity avg `0.0773` n `98`; fx avg `-0.0618` n `6`; index avg `0.0728` n `25`; metal avg `0.015` n `20`; unknown avg `-0.1066` n `773`
- 24h: commodity avg `0.631` n `12`; crypto_alt avg `-0.4785` n `230`; crypto_major avg `-0.6286` n `8`; equity avg `-0.584` n `98`; fx avg `-0.1011` n `6`; index avg `-0.0238` n `25`; metal avg `-0.0726` n `20`; unknown avg `1.7335` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0753`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0664`, n `666`, weak_sample_signal
