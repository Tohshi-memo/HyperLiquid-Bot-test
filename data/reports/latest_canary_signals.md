# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T11:23:02.031021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.2559` n `234`; crypto_major avg `-0.1298` n `8`; equity avg `-0.0085` n `140`; fx avg `-0.0156` n `6`; index avg `0.007` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.1661` n `943`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0371` n `234`; crypto_major avg `-0.0849` n `8`; equity avg `0.0027` n `140`; fx avg `0.0095` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0095` n `20`; unknown avg `0.3167` n `941`
- 4h: commodity avg `0.0344` n `12`; crypto_alt avg `-0.7708` n `234`; crypto_major avg `-0.3385` n `8`; equity avg `-0.0528` n `140`; fx avg `0.0163` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0124` n `20`; unknown avg `0.1426` n `935`
- 24h: commodity avg `0.245` n `12`; crypto_alt avg `-2.4908` n `234`; crypto_major avg `-2.4455` n `8`; equity avg `-0.2889` n `140`; fx avg `-0.0565` n `6`; index avg `-0.0486` n `26`; metal avg `-0.0163` n `20`; unknown avg `-0.0226` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
