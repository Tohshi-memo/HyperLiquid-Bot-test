# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T02:22:27.119229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2395` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1416` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0173` n `13`; crypto_alt avg `-0.8117` n `239`; crypto_major avg `-0.8103` n `8`; equity avg `-0.1729` n `162`; fx avg `0.0061` n `6`; index avg `-0.0133` n `27`; metal avg `-0.0256` n `20`; unknown avg `1.5786` n `1260`
- 1h: commodity avg `-0.0055` n `13`; crypto_alt avg `-1.2373` n `239`; crypto_major avg `-1.1575` n `8`; equity avg `-0.1984` n `162`; fx avg `-0.0043` n `6`; index avg `-0.0159` n `27`; metal avg `-0.0197` n `20`; unknown avg `8.3035` n `1258`
- 4h: commodity avg `0.0523` n `13`; crypto_alt avg `-0.9399` n `239`; crypto_major avg `-1.2815` n `8`; equity avg `-0.476` n `162`; fx avg `-0.0382` n `6`; index avg `-0.042` n `27`; metal avg `-0.023` n `20`; unknown avg `0.7679` n `1206`
- 24h: commodity avg `-0.1649` n `13`; crypto_alt avg `-2.5652` n `239`; crypto_major avg `-3.7599` n `8`; equity avg `-3.9945` n `162`; fx avg `-0.1014` n `6`; index avg `-0.3593` n `27`; metal avg `-0.5909` n `20`; unknown avg `65.2169` n `1036`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
