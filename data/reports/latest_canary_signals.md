# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T10:52:24.435254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0965` n `12`; crypto_alt avg `-0.1281` n `230`; crypto_major avg `-0.2758` n `8`; equity avg `-0.1216` n `98`; fx avg `-0.0143` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0525` n `20`; unknown avg `0.13` n `771`
- 1h: commodity avg `0.0051` n `12`; crypto_alt avg `-0.143` n `230`; crypto_major avg `-0.3532` n `8`; equity avg `-0.1122` n `98`; fx avg `-0.0151` n `6`; index avg `0.0085` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.1094` n `771`
- 4h: commodity avg `0.2747` n `12`; crypto_alt avg `-0.2185` n `230`; crypto_major avg `-0.0943` n `8`; equity avg `0.3586` n `98`; fx avg `0.0056` n `6`; index avg `0.0561` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0673` n `771`
- 24h: commodity avg `0.3977` n `12`; crypto_alt avg `2.1041` n `230`; crypto_major avg `2.3531` n `8`; equity avg `1.4864` n `98`; fx avg `-0.0976` n `6`; index avg `0.2549` n `25`; metal avg `0.6208` n `20`; unknown avg `0.2511` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0848`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0703`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0657`, n `666`, weak_sample_signal
