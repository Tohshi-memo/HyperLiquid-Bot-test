# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T08:37:27.389450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0607` n `12`; crypto_alt avg `-0.241` n `229`; crypto_major avg `-0.3011` n `8`; equity avg `-0.0596` n `88`; fx avg `0.0146` n `6`; index avg `-0.0177` n `25`; metal avg `-0.0999` n `20`; unknown avg `0.0137` n `765`
- 1h: commodity avg `-0.0393` n `12`; crypto_alt avg `-0.3913` n `229`; crypto_major avg `-0.4369` n `8`; equity avg `-0.034` n `88`; fx avg `0.004` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0669` n `20`; unknown avg `0.0183` n `765`
- 4h: commodity avg `0.0284` n `12`; crypto_alt avg `-0.7428` n `229`; crypto_major avg `-0.7142` n `8`; equity avg `-0.004` n `88`; fx avg `0.0476` n `6`; index avg `0.0478` n `25`; metal avg `0.04` n `20`; unknown avg `-0.1975` n `731`
- 24h: commodity avg `-0.2111` n `12`; crypto_alt avg `-0.4182` n `229`; crypto_major avg `0.4118` n `8`; equity avg `-0.7368` n `88`; fx avg `0.0906` n `6`; index avg `-0.0153` n `25`; metal avg `-0.2127` n `20`; unknown avg `1.102` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
