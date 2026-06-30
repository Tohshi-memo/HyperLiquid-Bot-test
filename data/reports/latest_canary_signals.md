# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T02:07:27.666638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2626` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `0.0277` n `228`; crypto_major avg `-0.0042` n `8`; equity avg `0.0373` n `88`; fx avg `-0.012` n `6`; index avg `0.0149` n `23`; metal avg `0.0738` n `20`; unknown avg `-0.0275` n `763`
- 1h: commodity avg `0.0346` n `12`; crypto_alt avg `0.0568` n `228`; crypto_major avg `0.0924` n `8`; equity avg `0.3564` n `88`; fx avg `-0.0352` n `6`; index avg `0.1181` n `23`; metal avg `0.314` n `20`; unknown avg `0.0871` n `763`
- 4h: commodity avg `0.0197` n `12`; crypto_alt avg `-1.0407` n `228`; crypto_major avg `-1.306` n `8`; equity avg `-0.1731` n `88`; fx avg `0.0423` n `6`; index avg `-0.0434` n `23`; metal avg `-0.4359` n `20`; unknown avg `0.2925` n `761`
- 24h: commodity avg `-0.2551` n `12`; crypto_alt avg `0.6787` n `228`; crypto_major avg `1.9558` n `8`; equity avg `2.0874` n `88`; fx avg `0.1745` n `6`; index avg `0.2702` n `23`; metal avg `-0.6587` n `20`; unknown avg `1.6067` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
