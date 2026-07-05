# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T21:45:16.675553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.0011` n `229`; crypto_major avg `0.0408` n `8`; equity avg `-0.0103` n `88`; fx avg `0.0006` n `6`; index avg `-0.0049` n `25`; metal avg `-0.0164` n `20`; unknown avg `-0.0045` n `765`
- 1h: commodity avg `0.0452` n `12`; crypto_alt avg `0.4026` n `229`; crypto_major avg `0.4517` n `8`; equity avg `-0.0025` n `88`; fx avg `0.0301` n `6`; index avg `-0.007` n `25`; metal avg `-0.0233` n `20`; unknown avg `0.2047` n `765`
- 4h: commodity avg `-0.0211` n `12`; crypto_alt avg `0.6944` n `229`; crypto_major avg `0.746` n `8`; equity avg `0.0975` n `88`; fx avg `0.0033` n `6`; index avg `0.0049` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.8544` n `765`
- 24h: commodity avg `0.0405` n `12`; crypto_alt avg `-0.6378` n `229`; crypto_major avg `-0.0428` n `8`; equity avg `0.3125` n `88`; fx avg `-0.0371` n `6`; index avg `0.0758` n `25`; metal avg `0.0001` n `20`; unknown avg `1.1717` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
