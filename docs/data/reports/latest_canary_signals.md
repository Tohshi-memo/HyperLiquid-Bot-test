# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T10:22:28.794158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3019` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0067` n `13`; crypto_alt avg `0.1551` n `238`; crypto_major avg `0.0907` n `8`; equity avg `0.0286` n `156`; fx avg `-0.0097` n `6`; index avg `0.0018` n `27`; metal avg `-0.0398` n `20`; unknown avg `158.8972` n `1261`
- 1h: commodity avg `0.0991` n `13`; crypto_alt avg `0.3385` n `238`; crypto_major avg `-0.0489` n `8`; equity avg `-0.2522` n `156`; fx avg `0.0071` n `6`; index avg `-0.0528` n `27`; metal avg `-0.1022` n `20`; unknown avg `0.2548` n `1255`
- 4h: commodity avg `0.2797` n `13`; crypto_alt avg `0.058` n `238`; crypto_major avg `-1.3525` n `8`; equity avg `-0.8842` n `156`; fx avg `0.0427` n `6`; index avg `-0.0506` n `27`; metal avg `-0.1412` n `20`; unknown avg `5.148` n `1190`
- 24h: commodity avg `0.2573` n `13`; crypto_alt avg `-3.3275` n `238`; crypto_major avg `-0.882` n `8`; equity avg `-3.5855` n `155`; fx avg `0.1157` n `6`; index avg `-0.4453` n `27`; metal avg `-0.7004` n `20`; unknown avg `30.8696` n `988`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
