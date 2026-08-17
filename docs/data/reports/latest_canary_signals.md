# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T11:46:02.541383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `0.0604` n `230`; crypto_major avg `0.0461` n `8`; equity avg `0.06` n `114`; fx avg `0.0013` n `6`; index avg `0.0083` n `25`; metal avg `-0.0324` n `20`; unknown avg `0.0003` n `792`
- 1h: commodity avg `-0.0603` n `12`; crypto_alt avg `0.1538` n `230`; crypto_major avg `0.0164` n `8`; equity avg `-0.147` n `114`; fx avg `0.0185` n `6`; index avg `-0.0049` n `25`; metal avg `-0.0042` n `20`; unknown avg `0.0612` n `792`
- 4h: commodity avg `0.042` n `12`; crypto_alt avg `0.0631` n `230`; crypto_major avg `0.1101` n `8`; equity avg `-0.0801` n `114`; fx avg `-0.0137` n `6`; index avg `-0.015` n `25`; metal avg `-0.0886` n `20`; unknown avg `0.0187` n `792`
- 24h: commodity avg `-0.1613` n `12`; crypto_alt avg `0.1609` n `230`; crypto_major avg `1.014` n `8`; equity avg `1.1838` n `114`; fx avg `-0.0159` n `6`; index avg `0.1477` n `25`; metal avg `0.1751` n `20`; unknown avg `0.0579` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
