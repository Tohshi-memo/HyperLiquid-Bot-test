# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T23:07:33.174968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.117` n `230`; crypto_major avg `-0.0957` n `8`; equity avg `0.0` n `98`; fx avg `0.0019` n `6`; index avg `0.0044` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.0435` n `771`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.2929` n `230`; crypto_major avg `-0.1589` n `8`; equity avg `-0.0364` n `98`; fx avg `-0.0018` n `6`; index avg `-0.0017` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.1644` n `771`
- 4h: commodity avg `0.0387` n `12`; crypto_alt avg `-0.3083` n `230`; crypto_major avg `-0.2474` n `8`; equity avg `0.7313` n `98`; fx avg `-0.0104` n `6`; index avg `0.0192` n `25`; metal avg `-0.0328` n `20`; unknown avg `-0.2665` n `771`
- 24h: commodity avg `0.4531` n `12`; crypto_alt avg `0.6571` n `230`; crypto_major avg `0.5596` n `8`; equity avg `4.2605` n `98`; fx avg `0.0622` n `6`; index avg `0.6596` n `25`; metal avg `0.7682` n `20`; unknown avg `0.1036` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0907`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0519`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0472`, n `666`, weak_sample_signal
