# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T17:37:33.074246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.031` n `13`; crypto_alt avg `-0.6431` n `239`; crypto_major avg `-0.6388` n `8`; equity avg `-1.0257` n `158`; fx avg `0.0041` n `6`; index avg `-0.1551` n `27`; metal avg `-0.0571` n `20`; unknown avg `4.3826` n `1257`
- 1h: commodity avg `-0.0125` n `13`; crypto_alt avg `-0.3575` n `239`; crypto_major avg `-0.452` n `8`; equity avg `-0.9573` n `158`; fx avg `-0.016` n `6`; index avg `-0.1569` n `27`; metal avg `-0.0835` n `20`; unknown avg `74.9996` n `1255`
- 4h: commodity avg `-0.2584` n `13`; crypto_alt avg `-0.3311` n `239`; crypto_major avg `-0.3228` n `8`; equity avg `-1.2272` n `158`; fx avg `0.0027` n `6`; index avg `-0.0975` n `27`; metal avg `0.0212` n `20`; unknown avg `10.2319` n `1245`
- 24h: commodity avg `0.069` n `13`; crypto_alt avg `1.9859` n `239`; crypto_major avg `-0.7798` n `8`; equity avg `1.0668` n `158`; fx avg `-0.1067` n `6`; index avg `0.0378` n `27`; metal avg `-0.3134` n `20`; unknown avg `56.2309` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
