# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T09:22:25.223835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1919` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0174` n `13`; crypto_alt avg `-0.3095` n `239`; crypto_major avg `-0.2784` n `8`; equity avg `-0.4914` n `162`; fx avg `-0.0044` n `6`; index avg `-0.0504` n `27`; metal avg `-0.0429` n `20`; unknown avg `188.8444` n `1264`
- 1h: commodity avg `0.0149` n `13`; crypto_alt avg `-0.6723` n `239`; crypto_major avg `-0.7031` n `8`; equity avg `-1.1361` n `162`; fx avg `-0.0431` n `6`; index avg `-0.1245` n `27`; metal avg `-0.0599` n `20`; unknown avg `25.5493` n `1262`
- 4h: commodity avg `0.2131` n `13`; crypto_alt avg `-1.0103` n `239`; crypto_major avg `-1.3268` n `8`; equity avg `-1.5098` n `162`; fx avg `-0.0375` n `6`; index avg `-0.1349` n `27`; metal avg `-0.2185` n `20`; unknown avg `-0.2641` n `1172`
- 24h: commodity avg `-0.759` n `13`; crypto_alt avg `0.3994` n `239`; crypto_major avg `0.9189` n `8`; equity avg `-3.3865` n `162`; fx avg `-0.0758` n `6`; index avg `-0.3725` n `27`; metal avg `-0.1766` n `20`; unknown avg `16.9838` n `1115`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
