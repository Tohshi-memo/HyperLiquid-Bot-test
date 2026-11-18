# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T08:52:33.806352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1067` n `13`; crypto_alt avg `0.1631` n `239`; crypto_major avg `-0.008` n `8`; equity avg `0.0307` n `163`; fx avg `-0.0153` n `6`; index avg `0.0137` n `27`; metal avg `-0.0053` n `20`; unknown avg `-0.0112` n `1240`
- 1h: commodity avg `-0.0738` n `13`; crypto_alt avg `0.0128` n `239`; crypto_major avg `-0.2354` n `8`; equity avg `-0.1798` n `163`; fx avg `-0.0466` n `6`; index avg `-0.0003` n `27`; metal avg `-0.1771` n `20`; unknown avg `6.5947` n `1198`
- 4h: commodity avg `-0.1887` n `13`; crypto_alt avg `0.8387` n `239`; crypto_major avg `0.5319` n `8`; equity avg `0.7192` n `163`; fx avg `-0.0939` n `6`; index avg `0.0923` n `27`; metal avg `-0.3202` n `20`; unknown avg `0.3157` n `1176`
- 24h: commodity avg `-0.1713` n `13`; crypto_alt avg `0.6701` n `239`; crypto_major avg `1.0782` n `8`; equity avg `1.0074` n `163`; fx avg `-0.1598` n `6`; index avg `0.098` n `27`; metal avg `-1.1181` n `20`; unknown avg `5.9052` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
