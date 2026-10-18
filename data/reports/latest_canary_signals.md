# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T16:07:26.636913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7364` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6614` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0036` n `13`; crypto_alt avg `0.0026` n `237`; crypto_major avg `-0.0582` n `8`; equity avg `-0.0104` n `151`; fx avg `-0.0089` n `6`; index avg `0.0031` n `26`; metal avg `-0.0` n `20`; unknown avg `-0.0217` n `1162`
- 1h: commodity avg `-0.0048` n `13`; crypto_alt avg `-0.3861` n `237`; crypto_major avg `-0.3418` n `8`; equity avg `-0.1583` n `151`; fx avg `-0.0059` n `6`; index avg `-0.0299` n `26`; metal avg `-0.0186` n `20`; unknown avg `0.0391` n `1161`
- 4h: commodity avg `0.0005` n `13`; crypto_alt avg `-1.5195` n `237`; crypto_major avg `-1.7856` n `8`; equity avg `-0.6216` n `151`; fx avg `-0.005` n `6`; index avg `-0.1242` n `26`; metal avg `-0.0492` n `20`; unknown avg `-0.2431` n `1159`
- 24h: commodity avg `-0.0099` n `13`; crypto_alt avg `-2.843` n `236`; crypto_major avg `-1.177` n `8`; equity avg `-0.8285` n `151`; fx avg `-0.0276` n `6`; index avg `-0.1206` n `26`; metal avg `-0.0556` n `20`; unknown avg `1.9641` n `1011`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.212`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1291`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
