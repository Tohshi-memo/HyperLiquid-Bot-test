# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T10:52:29.046364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1276` n `12`; crypto_alt avg `-0.1697` n `230`; crypto_major avg `-0.0777` n `8`; equity avg `0.1704` n `102`; fx avg `0.0142` n `6`; index avg `0.0334` n `25`; metal avg `-0.0108` n `20`; unknown avg `-0.0098` n `779`
- 1h: commodity avg `-0.2086` n `12`; crypto_alt avg `-0.1704` n `230`; crypto_major avg `0.0225` n `8`; equity avg `0.5907` n `102`; fx avg `-0.0411` n `6`; index avg `0.1121` n `25`; metal avg `0.0879` n `20`; unknown avg `0.0301` n `779`
- 4h: commodity avg `-0.4425` n `12`; crypto_alt avg `0.0549` n `230`; crypto_major avg `0.6739` n `8`; equity avg `1.3058` n `102`; fx avg `-0.0021` n `6`; index avg `0.2026` n `25`; metal avg `0.4399` n `20`; unknown avg `0.0134` n `771`
- 24h: commodity avg `0.1963` n `12`; crypto_alt avg `-0.1814` n `230`; crypto_major avg `0.0205` n `8`; equity avg `-2.1461` n `102`; fx avg `-0.0464` n `6`; index avg `-0.31` n `25`; metal avg `0.5035` n `20`; unknown avg `-0.0204` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
