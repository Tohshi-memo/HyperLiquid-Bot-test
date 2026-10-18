# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T16:37:24.904955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6087` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5428` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `-0.256` n `237`; crypto_major avg `-0.0706` n `8`; equity avg `-0.0676` n `151`; fx avg `-0.0006` n `6`; index avg `0.0011` n `26`; metal avg `0.0093` n `20`; unknown avg `0.132` n `1194`
- 1h: commodity avg `0.0043` n `13`; crypto_alt avg `-0.1108` n `237`; crypto_major avg `-0.1531` n `8`; equity avg `-0.0102` n `151`; fx avg `-0.0051` n `6`; index avg `0.0188` n `26`; metal avg `0.0014` n `20`; unknown avg `0.1162` n `1162`
- 4h: commodity avg `0.0216` n `13`; crypto_alt avg `-1.7843` n `237`; crypto_major avg `-1.6537` n `8`; equity avg `-0.6179` n `151`; fx avg `-0.0082` n `6`; index avg `-0.1109` n `26`; metal avg `-0.045` n `20`; unknown avg `0.0873` n `1159`
- 24h: commodity avg `0.0052` n `13`; crypto_alt avg `-2.7693` n `236`; crypto_major avg `-1.1325` n `8`; equity avg `-0.8644` n `151`; fx avg `-0.0193` n `6`; index avg `-0.1184` n `26`; metal avg `-0.0376` n `20`; unknown avg `1.4368` n `1017`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2117`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1287`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.08`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
