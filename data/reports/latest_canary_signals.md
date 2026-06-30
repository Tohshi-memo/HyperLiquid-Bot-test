# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T09:58:10.029856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0381` n `12`; crypto_alt avg `0.1013` n `228`; crypto_major avg `0.0947` n `8`; equity avg `0.0802` n `88`; fx avg `0.0005` n `6`; index avg `0.0241` n `23`; metal avg `0.1564` n `20`; unknown avg `0.0034` n `765`
- 1h: commodity avg `0.0741` n `12`; crypto_alt avg `0.1806` n `228`; crypto_major avg `0.184` n `8`; equity avg `0.1537` n `88`; fx avg `-0.0137` n `6`; index avg `0.0023` n `23`; metal avg `0.1744` n `20`; unknown avg `-0.1067` n `765`
- 4h: commodity avg `0.2872` n `12`; crypto_alt avg `-0.3818` n `228`; crypto_major avg `-0.3226` n `8`; equity avg `-0.3631` n `88`; fx avg `0.0442` n `6`; index avg `-0.1051` n `23`; metal avg `0.6157` n `20`; unknown avg `-0.3733` n `739`
- 24h: commodity avg `0.0052` n `12`; crypto_alt avg `-0.7495` n `228`; crypto_major avg `0.4986` n `8`; equity avg `1.4025` n `88`; fx avg `0.1228` n `6`; index avg `0.1257` n `23`; metal avg `0.3125` n `20`; unknown avg `9.23` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
