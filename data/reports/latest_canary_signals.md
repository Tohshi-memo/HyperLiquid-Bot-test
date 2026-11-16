# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T15:22:36.303856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `13`; crypto_alt avg `-0.3632` n `239`; crypto_major avg `-0.445` n `8`; equity avg `-0.1445` n `162`; fx avg `0.009` n `6`; index avg `0.0018` n `27`; metal avg `-0.0937` n `20`; unknown avg `0.8785` n `1265`
- 1h: commodity avg `-0.15` n `13`; crypto_alt avg `-0.3407` n `239`; crypto_major avg `-0.4578` n `8`; equity avg `-0.9821` n `162`; fx avg `0.0008` n `6`; index avg `-0.0805` n `27`; metal avg `-0.0996` n `20`; unknown avg `0.0282` n `1253`
- 4h: commodity avg `-0.5138` n `13`; crypto_alt avg `-0.7596` n `239`; crypto_major avg `-1.0282` n `8`; equity avg `-1.6566` n `162`; fx avg `0.0211` n `6`; index avg `-0.1517` n `27`; metal avg `-0.2261` n `20`; unknown avg `2.6843` n `1245`
- 24h: commodity avg `-0.8136` n `13`; crypto_alt avg `-0.6454` n `239`; crypto_major avg `-0.6419` n `8`; equity avg `-2.1606` n `162`; fx avg `-0.0166` n `6`; index avg `-0.183` n `27`; metal avg `-0.1378` n `20`; unknown avg `228.3087` n `1050`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
