# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T17:52:43.216531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.0823` n `230`; crypto_major avg `-0.2192` n `8`; equity avg `-0.0943` n `107`; fx avg `-0.0037` n `6`; index avg `-0.0108` n `25`; metal avg `-0.0343` n `20`; unknown avg `0.0801` n `782`
- 1h: commodity avg `-0.0919` n `12`; crypto_alt avg `0.119` n `230`; crypto_major avg `0.1076` n `8`; equity avg `0.3089` n `107`; fx avg `-0.0001` n `6`; index avg `0.0791` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.1479` n `782`
- 4h: commodity avg `-0.0841` n `12`; crypto_alt avg `0.1146` n `230`; crypto_major avg `0.1972` n `8`; equity avg `1.4143` n `107`; fx avg `0.0497` n `6`; index avg `0.281` n `25`; metal avg `0.1238` n `20`; unknown avg `-0.17` n `782`
- 24h: commodity avg `-1.1489` n `12`; crypto_alt avg `-0.2164` n `230`; crypto_major avg `0.1365` n `8`; equity avg `3.9963` n `107`; fx avg `0.0933` n `6`; index avg `0.7867` n `25`; metal avg `1.2026` n `20`; unknown avg `0.3522` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
