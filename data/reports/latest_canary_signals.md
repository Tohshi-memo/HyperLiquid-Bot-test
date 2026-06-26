# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T12:22:29.317608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6453` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3882` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `0.086` n `228`; crypto_major avg `0.1753` n `8`; equity avg `-0.0686` n `86`; fx avg `0.0091` n `6`; index avg `-0.004` n `23`; metal avg `-0.0406` n `20`; unknown avg `0.0427` n `765`
- 1h: commodity avg `0.0647` n `12`; crypto_alt avg `0.1058` n `228`; crypto_major avg `0.0739` n `8`; equity avg `-0.0604` n `86`; fx avg `-0.0081` n `6`; index avg `-0.0135` n `23`; metal avg `-0.1024` n `20`; unknown avg `0.0631` n `765`
- 4h: commodity avg `0.0522` n `12`; crypto_alt avg `-1.1116` n `228`; crypto_major avg `-1.4547` n `8`; equity avg `-0.4387` n `86`; fx avg `0.0151` n `6`; index avg `-0.0665` n `23`; metal avg `0.1906` n `20`; unknown avg `-0.0937` n `765`
- 24h: commodity avg `0.0873` n `12`; crypto_alt avg `-1.6334` n `228`; crypto_major avg `-1.6799` n `8`; equity avg `-4.1014` n `86`; fx avg `0.0766` n `6`; index avg `-0.6` n `23`; metal avg `0.561` n `20`; unknown avg `0.7842` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2831`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1946`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
