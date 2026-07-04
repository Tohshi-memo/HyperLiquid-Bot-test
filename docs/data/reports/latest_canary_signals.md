# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T21:12:18.157224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `0.1137` n `229`; crypto_major avg `0.0612` n `8`; equity avg `0.0007` n `88`; fx avg `0.0011` n `6`; index avg `-0.0099` n `25`; metal avg `0.0049` n `20`; unknown avg `-0.1027` n `765`
- 1h: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.1552` n `229`; crypto_major avg `-0.2061` n `8`; equity avg `-0.0119` n `88`; fx avg `0.0191` n `6`; index avg `-0.0105` n `25`; metal avg `0.0199` n `20`; unknown avg `-0.1798` n `765`
- 4h: commodity avg `-0.0348` n `12`; crypto_alt avg `-0.1873` n `229`; crypto_major avg `-0.0947` n `8`; equity avg `0.0976` n `88`; fx avg `-0.03` n `6`; index avg `0.0249` n `25`; metal avg `0.0569` n `20`; unknown avg `-0.9758` n `765`
- 24h: commodity avg `0.0452` n `12`; crypto_alt avg `0.2258` n `229`; crypto_major avg `0.3109` n `8`; equity avg `0.2618` n `88`; fx avg `-0.0279` n `6`; index avg `-0.0305` n `25`; metal avg `0.0889` n `20`; unknown avg `-0.378` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
