# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T01:52:26.493755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.059` n `12`; crypto_alt avg `0.1328` n `229`; crypto_major avg `0.1033` n `8`; equity avg `0.0809` n `88`; fx avg `0.023` n `6`; index avg `-0.0257` n `25`; metal avg `-0.086` n `20`; unknown avg `0.0421` n `765`
- 1h: commodity avg `0.0996` n `12`; crypto_alt avg `0.8809` n `229`; crypto_major avg `0.8794` n `8`; equity avg `0.9365` n `88`; fx avg `-0.0401` n `6`; index avg `0.2258` n `25`; metal avg `0.3642` n `20`; unknown avg `0.6395` n `765`
- 4h: commodity avg `0.085` n `12`; crypto_alt avg `0.9759` n `229`; crypto_major avg `0.8769` n `8`; equity avg `0.9504` n `88`; fx avg `0.0467` n `6`; index avg `0.1879` n `25`; metal avg `0.5814` n `20`; unknown avg `5.8476` n `765`
- 24h: commodity avg `0.3228` n `12`; crypto_alt avg `2.5244` n `228`; crypto_major avg `3.6082` n `8`; equity avg `-1.5724` n `88`; fx avg `-0.1071` n `6`; index avg `-0.3602` n `25`; metal avg `1.2543` n `20`; unknown avg `5.5843` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
