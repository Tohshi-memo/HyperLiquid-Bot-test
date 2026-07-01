# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T08:52:31.022243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3002` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0293` n `12`; crypto_alt avg `0.1686` n `228`; crypto_major avg `0.2511` n `8`; equity avg `0.1121` n `88`; fx avg `0.0051` n `6`; index avg `0.0122` n `23`; metal avg `0.0392` n `20`; unknown avg `-0.02` n `765`
- 1h: commodity avg `-0.229` n `12`; crypto_alt avg `0.0082` n `228`; crypto_major avg `-0.2261` n `8`; equity avg `0.0516` n `88`; fx avg `-0.013` n `6`; index avg `0.0166` n `23`; metal avg `0.0501` n `20`; unknown avg `0.1673` n `765`
- 4h: commodity avg `-0.3185` n `12`; crypto_alt avg `-1.1765` n `228`; crypto_major avg `-1.3793` n `8`; equity avg `-0.399` n `88`; fx avg `0.0311` n `6`; index avg `-0.0791` n `23`; metal avg `-0.0843` n `20`; unknown avg `-0.2912` n `743`
- 24h: commodity avg `-0.4146` n `12`; crypto_alt avg `-0.3997` n `228`; crypto_major avg `-0.5122` n `8`; equity avg `0.6924` n `88`; fx avg `0.0859` n `6`; index avg `0.02` n `23`; metal avg `-0.5872` n `20`; unknown avg `-0.2677` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
