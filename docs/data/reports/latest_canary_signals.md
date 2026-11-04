# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T20:52:29.307185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1146` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0205` n `13`; crypto_alt avg `-0.2519` n `239`; crypto_major avg `-0.2839` n `8`; equity avg `-0.145` n `158`; fx avg `-0.0094` n `6`; index avg `-0.0259` n `27`; metal avg `-0.0662` n `20`; unknown avg `1.7499` n `1240`
- 1h: commodity avg `0.0584` n `13`; crypto_alt avg `0.2727` n `239`; crypto_major avg `0.1631` n `8`; equity avg `0.0054` n `158`; fx avg `0.0119` n `6`; index avg `-0.0188` n `27`; metal avg `0.0211` n `20`; unknown avg `174.8869` n `1212`
- 4h: commodity avg `0.1882` n `13`; crypto_alt avg `-1.5404` n `239`; crypto_major avg `-1.2065` n `8`; equity avg `-0.5028` n `158`; fx avg `0.0281` n `6`; index avg `-0.0919` n `27`; metal avg `0.0579` n `20`; unknown avg `7.2991` n `1214`
- 24h: commodity avg `-1.7121` n `13`; crypto_alt avg `1.2746` n `239`; crypto_major avg `1.4999` n `8`; equity avg `-1.0688` n `158`; fx avg `0.0577` n `6`; index avg `0.1066` n `27`; metal avg `1.2843` n `20`; unknown avg `4.803` n `1095`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2662`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
