# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T14:36:22.515719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2855` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0336` n `13`; crypto_alt avg `-0.0216` n `238`; crypto_major avg `-0.151` n `8`; equity avg `0.1218` n `156`; fx avg `0.0242` n `6`; index avg `0.0472` n `27`; metal avg `0.1303` n `20`; unknown avg `0.7057` n `1235`
- 1h: commodity avg `0.1379` n `13`; crypto_alt avg `-0.4006` n `238`; crypto_major avg `-0.6105` n `8`; equity avg `-0.7177` n `156`; fx avg `-0.0247` n `6`; index avg `-0.0463` n `27`; metal avg `-0.0586` n `20`; unknown avg `2.7836` n `1159`
- 4h: commodity avg `0.0073` n `13`; crypto_alt avg `-0.7338` n `238`; crypto_major avg `-1.3581` n `8`; equity avg `-1.2888` n `156`; fx avg `-0.1267` n `6`; index avg `-0.0726` n `27`; metal avg `-0.3056` n `20`; unknown avg `2.8234` n `1149`
- 24h: commodity avg `0.6545` n `13`; crypto_alt avg `-5.8072` n `238`; crypto_major avg `-4.854` n `8`; equity avg `-5.416` n `156`; fx avg `-0.0515` n `6`; index avg `-0.4682` n `27`; metal avg `-0.9556` n `20`; unknown avg `91.5266` n `1036`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
