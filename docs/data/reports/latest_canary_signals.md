# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T12:07:28.495926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `0.1958` n `229`; crypto_major avg `0.0895` n `8`; equity avg `-0.0149` n `88`; fx avg `0.0191` n `6`; index avg `-0.007` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.0205` n `765`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.5397` n `229`; crypto_major avg `0.1268` n `8`; equity avg `-0.031` n `88`; fx avg `0.0128` n `6`; index avg `-0.0123` n `25`; metal avg `0.0004` n `20`; unknown avg `0.0215` n `765`
- 4h: commodity avg `0.0916` n `12`; crypto_alt avg `0.5153` n `229`; crypto_major avg `-0.145` n `8`; equity avg `-0.0209` n `88`; fx avg `0.0166` n `6`; index avg `0.0175` n `25`; metal avg `0.0127` n `20`; unknown avg `0.0181` n `765`
- 24h: commodity avg `0.1698` n `12`; crypto_alt avg `0.9395` n `229`; crypto_major avg `1.1502` n `8`; equity avg `0.0948` n `88`; fx avg `-0.0609` n `6`; index avg `-0.0508` n `25`; metal avg `-0.0808` n `20`; unknown avg `2.8565` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
