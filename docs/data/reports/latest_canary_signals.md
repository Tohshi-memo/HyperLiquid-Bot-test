# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T16:37:26.548302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.5228` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0459` n `12`; crypto_alt avg `0.2401` n `230`; crypto_major avg `0.1628` n `8`; equity avg `-0.041` n `121`; fx avg `-0.0021` n `6`; index avg `0.0001` n `25`; metal avg `0.0284` n `20`; unknown avg `0.1111` n `793`
- 1h: commodity avg `-0.0168` n `12`; crypto_alt avg `0.2301` n `230`; crypto_major avg `-0.0471` n `8`; equity avg `0.0054` n `121`; fx avg `0.0145` n `6`; index avg `-0.0106` n `25`; metal avg `0.0734` n `20`; unknown avg `1.3623` n `793`
- 4h: commodity avg `0.0425` n `12`; crypto_alt avg `0.9316` n `230`; crypto_major avg `1.0474` n `8`; equity avg `-0.4754` n `121`; fx avg `-0.0134` n `6`; index avg `-0.0688` n `25`; metal avg `0.1188` n `20`; unknown avg `1.463` n `793`
- 24h: commodity avg `0.2659` n `12`; crypto_alt avg `7.5595` n `230`; crypto_major avg `4.5161` n `8`; equity avg `1.3049` n `121`; fx avg `-0.1082` n `6`; index avg `0.0911` n `25`; metal avg `0.6492` n `20`; unknown avg `3.4781` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2372`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
