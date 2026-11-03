# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T16:07:53.678624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0435` n `13`; crypto_alt avg `0.0676` n `239`; crypto_major avg `-0.0878` n `8`; equity avg `0.1481` n `158`; fx avg `-0.001` n `6`; index avg `0.0225` n `27`; metal avg `-0.0318` n `20`; unknown avg `0.2814` n `1251`
- 1h: commodity avg `0.0473` n `13`; crypto_alt avg `0.2353` n `239`; crypto_major avg `0.2507` n `8`; equity avg `0.3861` n `158`; fx avg `-0.006` n `6`; index avg `0.0536` n `27`; metal avg `-0.0512` n `20`; unknown avg `14.0444` n `1251`
- 4h: commodity avg `-0.6664` n `13`; crypto_alt avg `0.9278` n `239`; crypto_major avg `1.1054` n `8`; equity avg `1.8416` n `158`; fx avg `0.0184` n `6`; index avg `0.2179` n `27`; metal avg `0.2661` n `20`; unknown avg `10.8029` n `1249`
- 24h: commodity avg `-0.3771` n `13`; crypto_alt avg `-0.1273` n `239`; crypto_major avg `0.5358` n `8`; equity avg `-0.729` n `158`; fx avg `0.0498` n `6`; index avg `-0.0659` n `27`; metal avg `-0.5569` n `20`; unknown avg `-0.3534` n `1021`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
