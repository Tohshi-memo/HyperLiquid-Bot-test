# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T21:52:27.943825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2149` n `12`; crypto_alt avg `0.1518` n `230`; crypto_major avg `0.1435` n `8`; equity avg `0.0273` n `102`; fx avg `-0.0007` n `6`; index avg `-0.0061` n `25`; metal avg `0.0351` n `20`; unknown avg `1.5454` n `783`
- 1h: commodity avg `-0.1825` n `12`; crypto_alt avg `0.2953` n `230`; crypto_major avg `0.3491` n `8`; equity avg `0.1719` n `102`; fx avg `0.0466` n `6`; index avg `0.0486` n `25`; metal avg `0.0579` n `20`; unknown avg `1.7378` n `783`
- 4h: commodity avg `-0.1394` n `12`; crypto_alt avg `0.3885` n `230`; crypto_major avg `0.6149` n `8`; equity avg `0.3976` n `102`; fx avg `0.1423` n `6`; index avg `0.065` n `25`; metal avg `0.1488` n `20`; unknown avg `2.2909` n `782`
- 24h: commodity avg `-1.3183` n `12`; crypto_alt avg `1.4263` n `230`; crypto_major avg `1.9473` n `8`; equity avg `1.537` n `102`; fx avg `-0.0144` n `6`; index avg `0.3371` n `25`; metal avg `0.3968` n `20`; unknown avg `1.5812` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
