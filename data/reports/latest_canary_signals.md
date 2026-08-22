# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T06:17:23.503838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.011` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.0053` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.8049` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `0.2046` n `230`; crypto_major avg `0.28` n `8`; equity avg `0.0039` n `121`; fx avg `-0.0004` n `6`; index avg `-0.0028` n `25`; metal avg `-0.0062` n `20`; unknown avg `0.048` n `794`
- 1h: commodity avg `0.0293` n `12`; crypto_alt avg `1.2745` n `230`; crypto_major avg `2.0403` n `8`; equity avg `0.2354` n `121`; fx avg `0.0091` n `6`; index avg `0.0001` n `25`; metal avg `0.035` n `20`; unknown avg `0.2047` n `778`
- 4h: commodity avg `0.0828` n `12`; crypto_alt avg `-2.3192` n `230`; crypto_major avg `-0.5337` n `8`; equity avg `-0.4514` n `121`; fx avg `0.0267` n `6`; index avg `-0.0498` n `25`; metal avg `-0.1301` n `20`; unknown avg `0.0085` n `777`
- 24h: commodity avg `0.2065` n `12`; crypto_alt avg `5.8638` n `230`; crypto_major avg `6.1062` n `8`; equity avg `-0.2048` n `121`; fx avg `0.0274` n `6`; index avg `-0.0652` n `25`; metal avg `0.0223` n `20`; unknown avg `1.1012` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
