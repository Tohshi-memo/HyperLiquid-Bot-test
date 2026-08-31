# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T08:22:24.123731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0573` n `12`; crypto_alt avg `-0.0443` n `232`; crypto_major avg `0.0239` n `8`; equity avg `-0.0586` n `128`; fx avg `-0.0231` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0531` n `20`; unknown avg `0.1065` n `793`
- 1h: commodity avg `0.1596` n `12`; crypto_alt avg `-0.3244` n `232`; crypto_major avg `-0.1543` n `8`; equity avg `-0.0671` n `128`; fx avg `-0.0403` n `6`; index avg `0.0024` n `26`; metal avg `-0.0436` n `20`; unknown avg `0.0332` n `791`
- 4h: commodity avg `0.013` n `12`; crypto_alt avg `0.8158` n `232`; crypto_major avg `0.8756` n `8`; equity avg `0.9826` n `128`; fx avg `-0.0875` n `6`; index avg `0.1892` n `26`; metal avg `0.1636` n `20`; unknown avg `0.3555` n `773`
- 24h: commodity avg `0.4084` n `12`; crypto_alt avg `-0.0214` n `231`; crypto_major avg `-1.4411` n `8`; equity avg `-0.2169` n `128`; fx avg `-0.1432` n `6`; index avg `-0.0301` n `26`; metal avg `-0.2494` n `20`; unknown avg `-0.3271` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
