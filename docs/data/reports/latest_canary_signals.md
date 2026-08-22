# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T02:03:24.548981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.3772` n `230`; crypto_major avg `0.2869` n `8`; equity avg `0.0163` n `121`; fx avg `0.002` n `6`; index avg `0.0032` n `25`; metal avg `-0.0098` n `20`; unknown avg `-0.0693` n `793`
- 1h: commodity avg `0.0316` n `12`; crypto_alt avg `0.1025` n `230`; crypto_major avg `0.1257` n `8`; equity avg `0.0026` n `121`; fx avg `0.0112` n `6`; index avg `0.0017` n `25`; metal avg `-0.0225` n `20`; unknown avg `-0.0533` n `793`
- 4h: commodity avg `-0.0313` n `12`; crypto_alt avg `1.0738` n `230`; crypto_major avg `-0.0611` n `8`; equity avg `-0.0134` n `121`; fx avg `0.0117` n `6`; index avg `0.0125` n `25`; metal avg `-0.0336` n `20`; unknown avg `0.1629` n `793`
- 24h: commodity avg `0.0231` n `12`; crypto_alt avg `8.9378` n `230`; crypto_major avg `6.5015` n `8`; equity avg `0.1907` n `121`; fx avg `0.0571` n `6`; index avg `0.0179` n `25`; metal avg `0.2965` n `20`; unknown avg `1.2081` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
