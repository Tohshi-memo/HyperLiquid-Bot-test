# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T19:37:34.380533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0336` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1297` n `13`; crypto_alt avg `-0.0899` n `239`; crypto_major avg `-0.1081` n `8`; equity avg `0.0072` n `158`; fx avg `-0.0053` n `6`; index avg `-0.0015` n `27`; metal avg `-0.037` n `20`; unknown avg `0.775` n `1264`
- 1h: commodity avg `-0.1149` n `13`; crypto_alt avg `-0.2431` n `239`; crypto_major avg `-0.2245` n `8`; equity avg `-0.1019` n `158`; fx avg `0.0047` n `6`; index avg `-0.0157` n `27`; metal avg `-0.0081` n `20`; unknown avg `0.6432` n `1258`
- 4h: commodity avg `-1.3113` n `13`; crypto_alt avg `-1.7036` n `239`; crypto_major avg `-1.1` n `8`; equity avg `-1.1966` n `158`; fx avg `-0.0365` n `6`; index avg `-0.0664` n `27`; metal avg `0.1871` n `20`; unknown avg `0.3435` n `1254`
- 24h: commodity avg `-1.7123` n `13`; crypto_alt avg `1.63` n `239`; crypto_major avg `2.1144` n `8`; equity avg `-0.7613` n `158`; fx avg `0.0352` n `6`; index avg `0.1368` n `27`; metal avg `1.2426` n `20`; unknown avg `0.7563` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2645`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
