# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T08:07:37.499881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `12`; crypto_alt avg `0.0875` n `230`; crypto_major avg `0.1642` n `8`; equity avg `0.1609` n `108`; fx avg `0.0241` n `6`; index avg `0.012` n `25`; metal avg `-0.0264` n `20`; unknown avg `0.0499` n `781`
- 1h: commodity avg `0.071` n `12`; crypto_alt avg `0.0106` n `230`; crypto_major avg `-0.0263` n `8`; equity avg `-0.2171` n `108`; fx avg `0.0267` n `6`; index avg `-0.0354` n `25`; metal avg `-0.0443` n `20`; unknown avg `0.0111` n `781`
- 4h: commodity avg `0.2808` n `12`; crypto_alt avg `0.3149` n `230`; crypto_major avg `0.3311` n `8`; equity avg `-0.0572` n `108`; fx avg `0.1031` n `6`; index avg `-0.0176` n `25`; metal avg `0.2455` n `20`; unknown avg `0.1166` n `749`
- 24h: commodity avg `-1.195` n `12`; crypto_alt avg `0.5888` n `230`; crypto_major avg `0.7209` n `8`; equity avg `2.8258` n `108`; fx avg `0.0033` n `6`; index avg `0.6496` n `25`; metal avg `1.1437` n `20`; unknown avg `0.0356` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
