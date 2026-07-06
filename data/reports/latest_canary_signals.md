# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T22:07:25.741346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.1196` n `229`; crypto_major avg `-0.2099` n `8`; equity avg `-0.0102` n `91`; fx avg `-0.0253` n `6`; index avg `-0.0037` n `25`; metal avg `-0.0169` n `20`; unknown avg `0.0413` n `763`
- 1h: commodity avg `0.006` n `12`; crypto_alt avg `0.4886` n `229`; crypto_major avg `0.4741` n `8`; equity avg `0.035` n `91`; fx avg `0.0109` n `6`; index avg `0.0003` n `25`; metal avg `0.0011` n `20`; unknown avg `0.0586` n `763`
- 4h: commodity avg `0.0596` n `12`; crypto_alt avg `0.568` n `229`; crypto_major avg `0.6683` n `8`; equity avg `0.1301` n `91`; fx avg `0.0064` n `6`; index avg `0.0301` n `25`; metal avg `0.0503` n `20`; unknown avg `-0.1769` n `763`
- 24h: commodity avg `0.068` n `12`; crypto_alt avg `0.8756` n `229`; crypto_major avg `0.5222` n `8`; equity avg `-0.6077` n `90`; fx avg `0.1268` n `6`; index avg `0.074` n `25`; metal avg `-0.2429` n `20`; unknown avg `-0.4027` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
