# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T00:37:29.593810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0237` n `12`; crypto_alt avg `-0.0226` n `230`; crypto_major avg `-0.0571` n `8`; equity avg `0.1009` n `114`; fx avg `0.003` n `6`; index avg `0.0383` n `25`; metal avg `0.0409` n `20`; unknown avg `-0.0116` n `793`
- 1h: commodity avg `-0.0317` n `12`; crypto_alt avg `-0.0531` n `230`; crypto_major avg `-0.0456` n `8`; equity avg `0.2405` n `114`; fx avg `-0.0216` n `6`; index avg `0.0261` n `25`; metal avg `0.1022` n `20`; unknown avg `-0.0831` n `793`
- 4h: commodity avg `-0.0165` n `12`; crypto_alt avg `-0.2546` n `230`; crypto_major avg `0.1972` n `8`; equity avg `0.4007` n `114`; fx avg `-0.0459` n `6`; index avg `0.043` n `25`; metal avg `0.1341` n `20`; unknown avg `-0.1962` n `792`
- 24h: commodity avg `0.5626` n `12`; crypto_alt avg `0.5017` n `230`; crypto_major avg `1.7078` n `8`; equity avg `1.4282` n `114`; fx avg `-0.0025` n `6`; index avg `0.081` n `25`; metal avg `0.2541` n `20`; unknown avg `0.323` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
