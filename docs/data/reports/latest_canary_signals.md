# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T20:07:16.898927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7251` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5814` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `0.0175` n `230`; crypto_major avg `0.0824` n `8`; equity avg `0.0111` n `121`; fx avg `-0.0026` n `6`; index avg `-0.0051` n `25`; metal avg `-0.0036` n `20`; unknown avg `0.0448` n `794`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `0.178` n `230`; crypto_major avg `0.4482` n `8`; equity avg `0.0485` n `121`; fx avg `0.0002` n `6`; index avg `-0.0045` n `25`; metal avg `0.0067` n `20`; unknown avg `0.0267` n `794`
- 4h: commodity avg `0.006` n `12`; crypto_alt avg `0.9447` n `230`; crypto_major avg `1.7278` n `8`; equity avg `0.1464` n `121`; fx avg `0.0209` n `6`; index avg `-0.0069` n `25`; metal avg `0.0027` n `20`; unknown avg `1.4605` n `794`
- 24h: commodity avg `0.0191` n `12`; crypto_alt avg `1.5368` n `230`; crypto_major avg `4.4216` n `8`; equity avg `-0.3555` n `121`; fx avg `0.0584` n `6`; index avg `-0.0471` n `25`; metal avg `-0.1239` n `20`; unknown avg `3.2236` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
