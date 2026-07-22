# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T10:22:30.040284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1427` n `12`; crypto_alt avg `0.1157` n `230`; crypto_major avg `0.1154` n `8`; equity avg `0.1359` n `98`; fx avg `0.0013` n `6`; index avg `0.0244` n `25`; metal avg `0.0224` n `20`; unknown avg `0.0127` n `773`
- 1h: commodity avg `-0.1342` n `12`; crypto_alt avg `0.0897` n `230`; crypto_major avg `0.1041` n `8`; equity avg `-0.0069` n `98`; fx avg `0.0203` n `6`; index avg `0.0219` n `25`; metal avg `0.0325` n `20`; unknown avg `0.0119` n `773`
- 4h: commodity avg `0.1372` n `12`; crypto_alt avg `0.522` n `230`; crypto_major avg `0.4529` n `8`; equity avg `0.287` n `98`; fx avg `-0.0169` n `6`; index avg `0.0591` n `25`; metal avg `-0.0502` n `20`; unknown avg `0.1278` n `772`
- 24h: commodity avg `0.6143` n `12`; crypto_alt avg `-0.6676` n `230`; crypto_major avg `-1.3786` n `8`; equity avg `0.5585` n `98`; fx avg `-0.0037` n `6`; index avg `0.0047` n `25`; metal avg `0.3042` n `20`; unknown avg `0.1152` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.103`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0785`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0687`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0679`, n `666`, weak_sample_signal
