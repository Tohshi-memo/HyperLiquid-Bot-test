# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T13:52:28.749564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0187` n `12`; crypto_alt avg `-0.2161` n `232`; crypto_major avg `-0.2624` n `8`; equity avg `-0.0791` n `128`; fx avg `0.0075` n `6`; index avg `-0.0214` n `26`; metal avg `-0.1175` n `20`; unknown avg `0.0108` n `794`
- 1h: commodity avg `0.1639` n `12`; crypto_alt avg `-0.1692` n `232`; crypto_major avg `-0.2216` n `8`; equity avg `0.2733` n `128`; fx avg `0.0116` n `6`; index avg `-0.0141` n `26`; metal avg `-0.1255` n `20`; unknown avg `-0.0278` n `792`
- 4h: commodity avg `0.0045` n `12`; crypto_alt avg `-0.728` n `232`; crypto_major avg `-0.6268` n `8`; equity avg `-0.005` n `128`; fx avg `0.0122` n `6`; index avg `-0.0546` n `26`; metal avg `-0.2034` n `20`; unknown avg `0.3227` n `792`
- 24h: commodity avg `0.6337` n `12`; crypto_alt avg `-1.9527` n `231`; crypto_major avg `-2.5503` n `8`; equity avg `-0.5166` n `128`; fx avg `-0.0972` n `6`; index avg `-0.1698` n `26`; metal avg `-0.4837` n `20`; unknown avg `-0.2952` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
