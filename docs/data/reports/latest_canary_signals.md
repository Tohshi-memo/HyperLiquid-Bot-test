# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T10:37:29.400133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0666` n `13`; crypto_alt avg `-0.1656` n `239`; crypto_major avg `0.1443` n `8`; equity avg `-0.0476` n `162`; fx avg `-0.0075` n `6`; index avg `-0.0063` n `27`; metal avg `0.0538` n `20`; unknown avg `0.0508` n `1265`
- 1h: commodity avg `0.1495` n `13`; crypto_alt avg `-0.0954` n `239`; crypto_major avg `0.4038` n `8`; equity avg `-0.2752` n `162`; fx avg `0.0247` n `6`; index avg `-0.0398` n `27`; metal avg `0.0891` n `20`; unknown avg `158.6738` n `1263`
- 4h: commodity avg `-0.2811` n `13`; crypto_alt avg `-0.205` n `239`; crypto_major avg `0.1202` n `8`; equity avg `-0.2204` n `162`; fx avg `-0.0321` n `6`; index avg `0.0224` n `27`; metal avg `0.1077` n `20`; unknown avg `34.7579` n `1095`
- 24h: commodity avg `-0.3683` n `13`; crypto_alt avg `-1.4579` n `239`; crypto_major avg `-1.0095` n `8`; equity avg `-0.995` n `162`; fx avg `-0.0624` n `6`; index avg `-0.0597` n `27`; metal avg `0.0354` n `20`; unknown avg `35.3549` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
