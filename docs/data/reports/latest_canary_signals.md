# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T11:22:28.942419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.025` n `12`; crypto_alt avg `0.0419` n `229`; crypto_major avg `0.0886` n `8`; equity avg `0.0915` n `88`; fx avg `0.0078` n `6`; index avg `0.0123` n `25`; metal avg `0.0397` n `20`; unknown avg `-0.0542` n `765`
- 1h: commodity avg `-0.0199` n `12`; crypto_alt avg `0.2163` n `229`; crypto_major avg `0.2307` n `8`; equity avg `-0.073` n `88`; fx avg `-0.0026` n `6`; index avg `0.0015` n `25`; metal avg `0.0809` n `20`; unknown avg `-0.0753` n `765`
- 4h: commodity avg `-0.0669` n `12`; crypto_alt avg `0.217` n `229`; crypto_major avg `0.0242` n `8`; equity avg `-0.065` n `88`; fx avg `-0.0173` n `6`; index avg `0.005` n `25`; metal avg `0.0654` n `20`; unknown avg `-0.1551` n `765`
- 24h: commodity avg `-0.152` n `12`; crypto_alt avg `0.4449` n `229`; crypto_major avg `0.9879` n `8`; equity avg `-0.7026` n `88`; fx avg `0.0785` n `6`; index avg `0.0004` n `25`; metal avg `-0.1347` n `20`; unknown avg `1.0397` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
