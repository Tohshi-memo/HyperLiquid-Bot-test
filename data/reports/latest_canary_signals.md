# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T01:22:26.477081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9003` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8726` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0348` n `12`; crypto_alt avg `-0.1591` n `230`; crypto_major avg `-0.1108` n `8`; equity avg `-0.0052` n `121`; fx avg `0.0009` n `6`; index avg `-0.0065` n `25`; metal avg `-0.0103` n `20`; unknown avg `0.0293` n `793`
- 1h: commodity avg `-0.0075` n `12`; crypto_alt avg `0.5136` n `230`; crypto_major avg `0.3138` n `8`; equity avg `-0.05` n `121`; fx avg `0.0038` n `6`; index avg `-0.01` n `25`; metal avg `-0.0073` n `20`; unknown avg `0.6666` n `793`
- 4h: commodity avg `-0.0305` n `12`; crypto_alt avg `2.0276` n `230`; crypto_major avg `1.8998` n `8`; equity avg `0.0272` n `121`; fx avg `-0.0081` n `6`; index avg `0.0227` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.6008` n `793`
- 24h: commodity avg `0.0576` n `12`; crypto_alt avg `9.3444` n `230`; crypto_major avg `6.9678` n `8`; equity avg `0.6648` n `121`; fx avg `0.0154` n `6`; index avg `0.0635` n `25`; metal avg `0.3291` n `20`; unknown avg `1.8604` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
