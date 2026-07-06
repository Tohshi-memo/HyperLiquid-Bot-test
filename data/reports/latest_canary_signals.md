# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T14:47:05.430717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6384` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2004` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.0007` n `229`; crypto_major avg `0.0639` n `8`; equity avg `-0.0371` n `88`; fx avg `-0.0051` n `6`; index avg `-0.0069` n `25`; metal avg `-0.1104` n `20`; unknown avg `-0.0705` n `765`
- 1h: commodity avg `0.1046` n `12`; crypto_alt avg `0.2996` n `229`; crypto_major avg `0.07` n `8`; equity avg `0.1679` n `88`; fx avg `0.0033` n `6`; index avg `0.0305` n `25`; metal avg `-0.1575` n `20`; unknown avg `0.0356` n `765`
- 4h: commodity avg `0.2313` n `12`; crypto_alt avg `-0.413` n `229`; crypto_major avg `-1.0897` n `8`; equity avg `0.5487` n `88`; fx avg `0.0315` n `6`; index avg `0.1107` n `25`; metal avg `-0.2961` n `20`; unknown avg `-0.2677` n `765`
- 24h: commodity avg `0.051` n `12`; crypto_alt avg `-0.434` n `229`; crypto_major avg `-0.9364` n `8`; equity avg `-0.1428` n `88`; fx avg `0.1749` n `6`; index avg `0.0587` n `25`; metal avg `-0.4427` n `20`; unknown avg `0.4908` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
