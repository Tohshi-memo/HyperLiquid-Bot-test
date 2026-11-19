# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T19:37:27.783635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1423` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0346` n `13`; crypto_alt avg `-0.0492` n `239`; crypto_major avg `-0.2855` n `8`; equity avg `0.0099` n `165`; fx avg `0.0053` n `6`; index avg `0.0225` n `27`; metal avg `-0.008` n `20`; unknown avg `0.4119` n `1262`
- 1h: commodity avg `-0.1401` n `13`; crypto_alt avg `-0.5987` n `239`; crypto_major avg `-1.1897` n `8`; equity avg `-0.5025` n `165`; fx avg `-0.013` n `6`; index avg `-0.0474` n `27`; metal avg `-0.1037` n `20`; unknown avg `2.7225` n `1260`
- 4h: commodity avg `-0.0588` n `13`; crypto_alt avg `-0.4201` n `239`; crypto_major avg `-0.3484` n `8`; equity avg `-1.3429` n `165`; fx avg `0.0013` n `6`; index avg `-0.1085` n `27`; metal avg `-0.0904` n `20`; unknown avg `2.0421` n `1251`
- 24h: commodity avg `-0.1521` n `13`; crypto_alt avg `-0.2292` n `239`; crypto_major avg `0.2257` n `8`; equity avg `-0.8343` n `165`; fx avg `0.0031` n `6`; index avg `0.0142` n `27`; metal avg `-0.3787` n `20`; unknown avg `5.2864` n `1158`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
