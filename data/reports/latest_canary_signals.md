# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T16:52:30.210071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2018` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0302` n `13`; crypto_alt avg `-0.3934` n `239`; crypto_major avg `-0.4257` n `8`; equity avg `-1.2603` n `165`; fx avg `-0.0239` n `6`; index avg `-0.1569` n `27`; metal avg `-0.0447` n `20`; unknown avg `10.035` n `1266`
- 1h: commodity avg `0.1316` n `13`; crypto_alt avg `-0.2965` n `239`; crypto_major avg `-0.0379` n `8`; equity avg `-0.1643` n `165`; fx avg `-0.0377` n `6`; index avg `-0.0447` n `27`; metal avg `0.0182` n `20`; unknown avg `5.3522` n `1257`
- 4h: commodity avg `0.0074` n `13`; crypto_alt avg `-1.7191` n `239`; crypto_major avg `-1.5628` n `8`; equity avg `-2.2678` n `165`; fx avg `-0.0305` n `6`; index avg `-0.361` n `27`; metal avg `-0.3548` n `20`; unknown avg `3.1899` n `1257`
- 24h: commodity avg `0.2929` n `13`; crypto_alt avg `0.2843` n `239`; crypto_major avg `1.0321` n `8`; equity avg `1.2581` n `165`; fx avg `0.0308` n `6`; index avg `0.1552` n `27`; metal avg `-0.3207` n `20`; unknown avg `4.2346` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
