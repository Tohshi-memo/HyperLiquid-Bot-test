# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T07:07:39.860498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.5371` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.5144` n `230`; crypto_major avg `0.7191` n `8`; equity avg `0.001` n `121`; fx avg `-0.0174` n `6`; index avg `0.0077` n `25`; metal avg `0.0062` n `20`; unknown avg `0.6229` n `794`
- 1h: commodity avg `-0.0107` n `12`; crypto_alt avg `1.4182` n `230`; crypto_major avg `1.5477` n `8`; equity avg `0.1572` n `121`; fx avg `-0.0206` n `6`; index avg `0.0182` n `25`; metal avg `0.0106` n `20`; unknown avg `0.7688` n `794`
- 4h: commodity avg `0.0718` n `12`; crypto_alt avg `-2.2302` n `230`; crypto_major avg `-0.5693` n `8`; equity avg `-0.3291` n `121`; fx avg `-0.0033` n `6`; index avg `-0.0341` n `25`; metal avg `-0.1125` n `20`; unknown avg `0.5799` n `777`
- 24h: commodity avg `0.19` n `12`; crypto_alt avg `6.9611` n `230`; crypto_major avg `7.5314` n `8`; equity avg `-0.3905` n `121`; fx avg `0.0016` n `6`; index avg `-0.075` n `25`; metal avg `-0.0117` n `20`; unknown avg `1.9198` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
