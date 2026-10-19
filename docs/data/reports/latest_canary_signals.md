# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T08:37:28.814127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0381` n `13`; crypto_alt avg `-0.029` n `237`; crypto_major avg `0.0844` n `8`; equity avg `0.0467` n `151`; fx avg `0.0208` n `6`; index avg `0.0147` n `26`; metal avg `-0.0085` n `20`; unknown avg `0.0698` n `1195`
- 1h: commodity avg `0.062` n `13`; crypto_alt avg `-0.2304` n `237`; crypto_major avg `-0.142` n `8`; equity avg `-0.1745` n `151`; fx avg `-0.0017` n `6`; index avg `-0.0139` n `26`; metal avg `-0.0941` n `20`; unknown avg `0.1574` n `1149`
- 4h: commodity avg `-0.0251` n `13`; crypto_alt avg `0.4909` n `237`; crypto_major avg `0.3019` n `8`; equity avg `0.0363` n `151`; fx avg `-0.0549` n `6`; index avg `0.0094` n `26`; metal avg `-0.1119` n `20`; unknown avg `0.2656` n `1124`
- 24h: commodity avg `-0.4503` n `13`; crypto_alt avg `0.8542` n `237`; crypto_major avg `1.4304` n `8`; equity avg `2.6089` n `151`; fx avg `-0.0533` n `6`; index avg `0.4791` n `26`; metal avg `0.2166` n `20`; unknown avg `2.6013` n `875`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1976`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1447`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1255`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0629`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
