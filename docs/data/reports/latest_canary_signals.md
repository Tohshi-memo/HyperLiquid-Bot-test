# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T16:22:25.605454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6367` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5745` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `0.114` n `237`; crypto_major avg `-0.0193` n `8`; equity avg `0.0747` n `151`; fx avg `0.0029` n `6`; index avg `0.0067` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.0257` n `1194`
- 1h: commodity avg `0.0098` n `13`; crypto_alt avg `0.008` n `237`; crypto_major avg `-0.2784` n `8`; equity avg `-0.0054` n `151`; fx avg `-0.003` n `6`; index avg `-0.0136` n `26`; metal avg `-0.0121` n `20`; unknown avg `-0.2121` n `1162`
- 4h: commodity avg `0.0005` n `13`; crypto_alt avg `-1.4475` n `237`; crypto_major avg `-1.6979` n `8`; equity avg `-0.5876` n `151`; fx avg `-0.0061` n `6`; index avg `-0.1234` n `26`; metal avg `-0.0612` n `20`; unknown avg `-0.2304` n `1159`
- 24h: commodity avg `0.0079` n `13`; crypto_alt avg `-2.793` n `236`; crypto_major avg `-1.1684` n `8`; equity avg `-0.7994` n `151`; fx avg `-0.0119` n `6`; index avg `-0.1125` n `26`; metal avg `-0.058` n `20`; unknown avg `1.9764` n `1011`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2122`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1291`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0801`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
