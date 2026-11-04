# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T00:37:22.982875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.293` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.2182` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0239` n `13`; crypto_alt avg `-0.4342` n `239`; crypto_major avg `-0.4194` n `8`; equity avg `-0.6888` n `158`; fx avg `0.0024` n `6`; index avg `-0.1033` n `27`; metal avg `-0.1536` n `20`; unknown avg `0.7673` n `1264`
- 1h: commodity avg `0.0669` n `13`; crypto_alt avg `-1.5743` n `239`; crypto_major avg `-1.5348` n `8`; equity avg `-1.6688` n `158`; fx avg `0.0222` n `6`; index avg `-0.2418` n `27`; metal avg `-0.1368` n `20`; unknown avg `2.2119` n `1252`
- 4h: commodity avg `0.0014` n `13`; crypto_alt avg `-1.0445` n `239`; crypto_major avg `-1.3314` n `8`; equity avg `-0.6885` n `158`; fx avg `0.031` n `6`; index avg `-0.1132` n `27`; metal avg `-0.0428` n `20`; unknown avg `1.1058` n `1171`
- 24h: commodity avg `0.351` n `13`; crypto_alt avg `-0.4619` n `239`; crypto_major avg `-0.5285` n `8`; equity avg `0.5534` n `158`; fx avg `0.1476` n `6`; index avg `-0.0113` n `27`; metal avg `-0.7176` n `20`; unknown avg `-0.0909` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
