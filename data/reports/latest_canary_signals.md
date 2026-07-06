# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T07:22:28.294096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `12`; crypto_alt avg `0.1633` n `229`; crypto_major avg `0.0897` n `8`; equity avg `0.0028` n `88`; fx avg `0.0103` n `6`; index avg `0.007` n `25`; metal avg `0.1044` n `20`; unknown avg `0.0487` n `765`
- 1h: commodity avg `-0.0873` n `12`; crypto_alt avg `0.1614` n `229`; crypto_major avg `0.1048` n `8`; equity avg `0.1487` n `88`; fx avg `0.012` n `6`; index avg `0.0447` n `25`; metal avg `0.0898` n `20`; unknown avg `-0.0097` n `763`
- 4h: commodity avg `0.1843` n `12`; crypto_alt avg `-0.6589` n `229`; crypto_major avg `-0.3781` n `8`; equity avg `0.4634` n `88`; fx avg `0.0282` n `6`; index avg `0.1426` n `25`; metal avg `0.0243` n `20`; unknown avg `-0.0083` n `731`
- 24h: commodity avg `-0.0734` n `12`; crypto_alt avg `0.0263` n `229`; crypto_major avg `0.9365` n `8`; equity avg `-0.6033` n `88`; fx avg `0.0941` n `6`; index avg `-0.0173` n `25`; metal avg `-0.1742` n `20`; unknown avg `1.1522` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
