# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T17:03:27.700895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5314` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0589` n `13`; crypto_alt avg `-0.0601` n `238`; crypto_major avg `-0.0812` n `8`; equity avg `-0.0456` n `156`; fx avg `0.0049` n `6`; index avg `0.0038` n `27`; metal avg `0.0564` n `20`; unknown avg `0.6541` n `1230`
- 1h: commodity avg `0.1282` n `13`; crypto_alt avg `-0.7555` n `238`; crypto_major avg `-0.5561` n `8`; equity avg `-0.4321` n `156`; fx avg `0.0005` n `6`; index avg `-0.026` n `27`; metal avg `0.0119` n `20`; unknown avg `2.7474` n `1230`
- 4h: commodity avg `0.2719` n `13`; crypto_alt avg `1.385` n `238`; crypto_major avg `1.5291` n `8`; equity avg `0.3511` n `156`; fx avg `0.1311` n `6`; index avg `-0.0277` n `27`; metal avg `-0.0023` n `20`; unknown avg `1.2384` n `1130`
- 24h: commodity avg `-0.6533` n `13`; crypto_alt avg `1.3831` n `238`; crypto_major avg `2.8356` n `8`; equity avg `-0.6328` n `155`; fx avg `0.0179` n `6`; index avg `-0.1449` n `27`; metal avg `-0.4203` n `20`; unknown avg `13.4176` n `944`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
