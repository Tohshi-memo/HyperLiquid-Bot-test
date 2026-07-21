# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T12:07:30.795190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0912` n `12`; crypto_alt avg `0.0855` n `230`; crypto_major avg `0.0135` n `8`; equity avg `0.0793` n `98`; fx avg `0.0011` n `6`; index avg `0.0219` n `25`; metal avg `0.0365` n `20`; unknown avg `-0.0043` n `771`
- 1h: commodity avg `-0.0446` n `12`; crypto_alt avg `0.1541` n `230`; crypto_major avg `0.2204` n `8`; equity avg `0.1694` n `98`; fx avg `0.0031` n `6`; index avg `0.0126` n `25`; metal avg `0.0475` n `20`; unknown avg `-0.0193` n `771`
- 4h: commodity avg `0.3613` n `12`; crypto_alt avg `0.0036` n `230`; crypto_major avg `0.0471` n `8`; equity avg `0.1133` n `98`; fx avg `-0.0236` n `6`; index avg `0.0506` n `25`; metal avg `-0.0253` n `20`; unknown avg `0.0319` n `771`
- 24h: commodity avg `0.3706` n `12`; crypto_alt avg `1.7364` n `230`; crypto_major avg `1.8915` n `8`; equity avg `1.1581` n `98`; fx avg `-0.0741` n `6`; index avg `0.1964` n `25`; metal avg `0.6219` n `20`; unknown avg `0.127` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0878`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.063`, n `666`, weak_sample_signal
