# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T09:22:28.263021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2267` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.028` n `13`; crypto_alt avg `-0.1324` n `238`; crypto_major avg `-0.2009` n `8`; equity avg `-0.2939` n `156`; fx avg `0.0076` n `6`; index avg `-0.0424` n `27`; metal avg `-0.004` n `20`; unknown avg `-0.2044` n `1261`
- 1h: commodity avg `0.0416` n `13`; crypto_alt avg `-0.3386` n `238`; crypto_major avg `-0.5131` n `8`; equity avg `-0.0623` n `156`; fx avg `0.0333` n `6`; index avg `0.0016` n `27`; metal avg `0.0465` n `20`; unknown avg `14.5166` n `1255`
- 4h: commodity avg `0.2146` n `13`; crypto_alt avg `-0.3857` n `238`; crypto_major avg `-1.2404` n `8`; equity avg `-0.8428` n `156`; fx avg `0.0317` n `6`; index avg `-0.0137` n `27`; metal avg `-0.1573` n `20`; unknown avg `2.4183` n `1172`
- 24h: commodity avg `0.0712` n `13`; crypto_alt avg `-3.7655` n `238`; crypto_major avg `-1.1395` n `8`; equity avg `-3.4499` n `155`; fx avg `0.1525` n `6`; index avg `-0.3769` n `27`; metal avg `-0.5885` n `20`; unknown avg `29.4955` n `946`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
