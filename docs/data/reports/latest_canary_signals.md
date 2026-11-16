# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T03:07:28.781660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `13`; crypto_alt avg `-0.0459` n `239`; crypto_major avg `0.1579` n `8`; equity avg `0.1199` n `162`; fx avg `-0.0044` n `6`; index avg `0.0108` n `27`; metal avg `0.0363` n `20`; unknown avg `0.2407` n `1257`
- 1h: commodity avg `-0.1209` n `13`; crypto_alt avg `0.5799` n `239`; crypto_major avg `0.3192` n `8`; equity avg `0.0313` n `162`; fx avg `-0.0075` n `6`; index avg `-0.0301` n `27`; metal avg `-0.0654` n `20`; unknown avg `-0.1021` n `1259`
- 4h: commodity avg `-0.0741` n `13`; crypto_alt avg `-0.2269` n `239`; crypto_major avg `-0.5567` n `8`; equity avg `-0.7891` n `162`; fx avg `-0.0257` n `6`; index avg `-0.1704` n `27`; metal avg `-0.3486` n `20`; unknown avg `0.3931` n `1239`
- 24h: commodity avg `-0.4887` n `13`; crypto_alt avg `0.1576` n `239`; crypto_major avg `0.2783` n `8`; equity avg `0.4842` n `162`; fx avg `-0.0155` n `6`; index avg `0.0496` n `27`; metal avg `0.1343` n `20`; unknown avg `1.0699` n `1123`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
