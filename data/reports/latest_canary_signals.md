# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T04:07:27.515370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0282` n `12`; crypto_alt avg `-0.0659` n `230`; crypto_major avg `-0.0555` n `8`; equity avg `-0.0176` n `112`; fx avg `-0.0059` n `6`; index avg `-0.0072` n `25`; metal avg `0.0549` n `20`; unknown avg `-0.0315` n `782`
- 1h: commodity avg `0.0749` n `12`; crypto_alt avg `-0.3065` n `230`; crypto_major avg `-0.2488` n `8`; equity avg `-0.1891` n `112`; fx avg `-0.0088` n `6`; index avg `-0.0472` n `25`; metal avg `0.0456` n `20`; unknown avg `-0.3602` n `782`
- 4h: commodity avg `0.0336` n `12`; crypto_alt avg `-0.2974` n `230`; crypto_major avg `-0.3874` n `8`; equity avg `-0.1797` n `112`; fx avg `-0.0555` n `6`; index avg `-0.1967` n `25`; metal avg `0.1378` n `20`; unknown avg `-0.1919` n `782`
- 24h: commodity avg `0.6797` n `12`; crypto_alt avg `0.3513` n `230`; crypto_major avg `-0.7401` n `8`; equity avg `0.7806` n `109`; fx avg `0.0147` n `6`; index avg `-0.1407` n `25`; metal avg `-0.0093` n `20`; unknown avg `113.195` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
