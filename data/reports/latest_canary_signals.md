# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T18:22:26.993548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7573` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6701` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0246` n `13`; crypto_alt avg `-0.3395` n `239`; crypto_major avg `-0.3298` n `8`; equity avg `-0.084` n `162`; fx avg `0.0072` n `6`; index avg `-0.0101` n `27`; metal avg `-0.0219` n `20`; unknown avg `0.7437` n `1260`
- 1h: commodity avg `-0.0011` n `13`; crypto_alt avg `-0.416` n `239`; crypto_major avg `0.144` n `8`; equity avg `-0.1163` n `162`; fx avg `0.0078` n `6`; index avg `-0.0128` n `27`; metal avg `-0.0302` n `20`; unknown avg `0.9445` n `1260`
- 4h: commodity avg `-0.0706` n `13`; crypto_alt avg `-1.9976` n `239`; crypto_major avg `-1.8276` n `8`; equity avg `-0.5976` n `162`; fx avg `0.0152` n `6`; index avg `-0.0703` n `27`; metal avg `-0.1575` n `20`; unknown avg `0.1826` n `1248`
- 24h: commodity avg `-0.0123` n `13`; crypto_alt avg `-6.9642` n `239`; crypto_major avg `-6.552` n `8`; equity avg `-1.5153` n `162`; fx avg `-0.0179` n `6`; index avg `-0.0984` n `27`; metal avg `-0.3406` n `20`; unknown avg `1.5245` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
