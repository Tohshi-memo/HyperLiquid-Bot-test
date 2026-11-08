# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T21:52:30.238976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2368` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.1761` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1694` n `13`; crypto_alt avg `-0.9334` n `239`; crypto_major avg `-0.9916` n `8`; equity avg `-0.3195` n `158`; fx avg `-0.0231` n `6`; index avg `-0.0254` n `27`; metal avg `-0.0275` n `20`; unknown avg `1.3521` n `1260`
- 1h: commodity avg `-0.0761` n `13`; crypto_alt avg `-1.2081` n `239`; crypto_major avg `-1.2786` n `8`; equity avg `-0.3647` n `158`; fx avg `-0.0253` n `6`; index avg `-0.0418` n `27`; metal avg `-0.027` n `20`; unknown avg `0.5583` n `1238`
- 4h: commodity avg `-0.2016` n `13`; crypto_alt avg `-0.8962` n `239`; crypto_major avg `-1.2602` n `8`; equity avg `-0.5307` n `158`; fx avg `-0.0545` n `6`; index avg `-0.0841` n `27`; metal avg `-0.0231` n `20`; unknown avg `14.5021` n `1162`
- 24h: commodity avg `-0.1909` n `13`; crypto_alt avg `-2.2591` n `239`; crypto_major avg `-1.3835` n `8`; equity avg `-0.302` n `158`; fx avg `0.012` n `6`; index avg `-0.0894` n `27`; metal avg `-0.0506` n `20`; unknown avg `-0.6358` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
