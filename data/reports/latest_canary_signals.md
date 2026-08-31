# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T09:07:25.784041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `-0.062` n `232`; crypto_major avg `0.0294` n `8`; equity avg `-0.0786` n `128`; fx avg `0.0173` n `6`; index avg `-0.0069` n `26`; metal avg `0.0335` n `20`; unknown avg `0.0169` n `791`
- 1h: commodity avg `0.195` n `12`; crypto_alt avg `0.0129` n `232`; crypto_major avg `0.3918` n `8`; equity avg `-0.164` n `128`; fx avg `-0.0101` n `6`; index avg `-0.0121` n `26`; metal avg `-0.0301` n `20`; unknown avg `0.3585` n `791`
- 4h: commodity avg `0.0992` n `12`; crypto_alt avg `0.6198` n `232`; crypto_major avg `0.9615` n `8`; equity avg `0.4315` n `128`; fx avg `-0.0933` n `6`; index avg `0.0713` n `26`; metal avg `0.1352` n `20`; unknown avg `0.6555` n `773`
- 24h: commodity avg `0.5432` n `12`; crypto_alt avg `0.0168` n `231`; crypto_major avg `-1.048` n `8`; equity avg `-0.3295` n `128`; fx avg `-0.1333` n `6`; index avg `-0.0312` n `26`; metal avg `-0.2207` n `20`; unknown avg `-0.3229` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
