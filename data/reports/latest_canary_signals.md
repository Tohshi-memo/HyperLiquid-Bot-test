# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T01:37:28.080287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.0918` n `230`; crypto_major avg `0.0161` n `8`; equity avg `0.0948` n `108`; fx avg `-0.0156` n `6`; index avg `0.0068` n `25`; metal avg `0.0752` n `20`; unknown avg `-0.0542` n `782`
- 1h: commodity avg `0.1658` n `12`; crypto_alt avg `-0.2392` n `230`; crypto_major avg `-0.2644` n `8`; equity avg `-0.4236` n `108`; fx avg `-0.0559` n `6`; index avg `-0.1029` n `25`; metal avg `0.0113` n `20`; unknown avg `-0.1651` n `782`
- 4h: commodity avg `0.068` n `12`; crypto_alt avg `0.1144` n `230`; crypto_major avg `-0.1636` n `8`; equity avg `-0.5413` n `108`; fx avg `-0.0696` n `6`; index avg `-0.1771` n `25`; metal avg `0.2068` n `20`; unknown avg `-0.084` n `782`
- 24h: commodity avg `-0.0737` n `12`; crypto_alt avg `0.2506` n `230`; crypto_major avg `0.3552` n `8`; equity avg `-1.8582` n `108`; fx avg `-0.0395` n `6`; index avg `-0.3561` n `25`; metal avg `1.0041` n `20`; unknown avg `1.0143` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
