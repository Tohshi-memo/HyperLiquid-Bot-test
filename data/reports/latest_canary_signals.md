# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T17:52:24.832617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `0.2506` n `229`; crypto_major avg `0.3802` n `8`; equity avg `0.0539` n `88`; fx avg `0.0078` n `6`; index avg `0.0078` n `25`; metal avg `0.0098` n `20`; unknown avg `0.0278` n `765`
- 1h: commodity avg `0.0208` n `12`; crypto_alt avg `0.4489` n `229`; crypto_major avg `0.5759` n `8`; equity avg `0.064` n `88`; fx avg `0.0087` n `6`; index avg `-0.0044` n `25`; metal avg `0.008` n `20`; unknown avg `0.5085` n `765`
- 4h: commodity avg `0.026` n `12`; crypto_alt avg `1.3802` n `229`; crypto_major avg `1.528` n `8`; equity avg `0.1353` n `88`; fx avg `0.0346` n `6`; index avg `-0.0167` n `25`; metal avg `0.0284` n `20`; unknown avg `0.8865` n `765`
- 24h: commodity avg `-0.0003` n `12`; crypto_alt avg `1.6328` n `229`; crypto_major avg `2.2488` n `8`; equity avg `0.2687` n `88`; fx avg `0.0006` n `6`; index avg `-0.081` n `25`; metal avg `0.0412` n `20`; unknown avg `1.9379` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
