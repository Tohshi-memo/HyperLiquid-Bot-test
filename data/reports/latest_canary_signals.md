# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T10:37:27.212077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0141` n `12`; crypto_alt avg `0.0315` n `229`; crypto_major avg `-0.0831` n `8`; equity avg `0.0054` n `88`; fx avg `0.0006` n `6`; index avg `0.0021` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0155` n `765`
- 1h: commodity avg `0.0546` n `12`; crypto_alt avg `0.1889` n `229`; crypto_major avg `0.0327` n `8`; equity avg `0.0723` n `88`; fx avg `-0.0026` n `6`; index avg `0.0222` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0998` n `765`
- 4h: commodity avg `0.0916` n `12`; crypto_alt avg `-0.259` n `229`; crypto_major avg `-0.1902` n `8`; equity avg `0.0177` n `88`; fx avg `-0.0076` n `6`; index avg `0.0098` n `25`; metal avg `0.0043` n `20`; unknown avg `0.3163` n `765`
- 24h: commodity avg `0.1387` n `12`; crypto_alt avg `0.8826` n `229`; crypto_major avg `1.4989` n `8`; equity avg `0.2386` n `88`; fx avg `-0.067` n `6`; index avg `-0.014` n `25`; metal avg `-0.085` n `20`; unknown avg `3.3048` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
