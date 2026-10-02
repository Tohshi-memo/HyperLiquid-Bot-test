# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T15:37:34.699925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.69` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.6867` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5858` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0455` n `13`; crypto_alt avg `0.1279` n `235`; crypto_major avg `-0.0748` n `8`; equity avg `0.0443` n `143`; fx avg `-0.0092` n `6`; index avg `0.0221` n `26`; metal avg `-0.0213` n `20`; unknown avg `8.71` n `984`
- 1h: commodity avg `0.2247` n `13`; crypto_alt avg `-0.3049` n `235`; crypto_major avg `-0.6641` n `8`; equity avg `-0.7653` n `143`; fx avg `-0.0055` n `6`; index avg `-0.1425` n `26`; metal avg `-0.3104` n `20`; unknown avg `7.3319` n `980`
- 4h: commodity avg `0.1705` n `13`; crypto_alt avg `-0.182` n `235`; crypto_major avg `-1.502` n `8`; equity avg `0.1847` n `142`; fx avg `0.0428` n `6`; index avg `0.0838` n `26`; metal avg `-0.3615` n `20`; unknown avg `1.402` n `934`
- 24h: commodity avg `-0.6437` n `13`; crypto_alt avg `2.7249` n `235`; crypto_major avg `1.3084` n `8`; equity avg `1.9498` n `142`; fx avg `-0.1223` n `6`; index avg `0.5258` n `26`; metal avg `-0.1467` n `20`; unknown avg `102.0964` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
