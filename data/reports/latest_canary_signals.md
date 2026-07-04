# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T13:37:28.777295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.2572` n `229`; crypto_major avg `-0.2692` n `8`; equity avg `-0.0537` n `88`; fx avg `0.0005` n `6`; index avg `0.0019` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.0261` n `765`
- 1h: commodity avg `-0.0493` n `12`; crypto_alt avg `-0.0973` n `229`; crypto_major avg `0.0346` n `8`; equity avg `-0.0274` n `88`; fx avg `-0.0014` n `6`; index avg `-0.0179` n `25`; metal avg `0.023` n `20`; unknown avg `0.0206` n `759`
- 4h: commodity avg `0.0387` n `12`; crypto_alt avg `0.7803` n `229`; crypto_major avg `0.286` n `8`; equity avg `-0.0489` n `88`; fx avg `0.0032` n `6`; index avg `0.017` n `25`; metal avg `0.0147` n `20`; unknown avg `-0.127` n `759`
- 24h: commodity avg `0.0194` n `12`; crypto_alt avg `0.6726` n `229`; crypto_major avg `1.27` n `8`; equity avg `0.2139` n `88`; fx avg `-0.0611` n `6`; index avg `-0.0462` n `25`; metal avg `0.0655` n `20`; unknown avg `2.2643` n `741`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
