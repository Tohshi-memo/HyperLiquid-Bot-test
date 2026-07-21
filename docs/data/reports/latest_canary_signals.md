# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T07:37:28.003070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1062` n `12`; crypto_alt avg `0.0837` n `230`; crypto_major avg `0.1029` n `8`; equity avg `0.0399` n `98`; fx avg `-0.0002` n `6`; index avg `0.0112` n `25`; metal avg `0.0508` n `20`; unknown avg `-0.0357` n `771`
- 1h: commodity avg `0.044` n `12`; crypto_alt avg `-0.1016` n `230`; crypto_major avg `-0.1025` n `8`; equity avg `0.0914` n `98`; fx avg `0.0203` n `6`; index avg `-0.0026` n `25`; metal avg `0.124` n `20`; unknown avg `-0.026` n `771`
- 4h: commodity avg `0.0832` n `12`; crypto_alt avg `0.5263` n `230`; crypto_major avg `0.547` n `8`; equity avg `0.5989` n `98`; fx avg `0.0255` n `6`; index avg `0.0668` n `25`; metal avg `0.4564` n `20`; unknown avg `0.0764` n `755`
- 24h: commodity avg `-0.0756` n `12`; crypto_alt avg `2.7965` n `230`; crypto_major avg `2.8463` n `8`; equity avg `1.6402` n `98`; fx avg `-0.1077` n `6`; index avg `0.3027` n `25`; metal avg `0.6938` n `20`; unknown avg `0.2269` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.076`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
