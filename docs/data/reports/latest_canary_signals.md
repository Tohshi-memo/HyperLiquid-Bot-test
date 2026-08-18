# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T00:07:27.275189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `-0.1135` n `230`; crypto_major avg `-0.1025` n `8`; equity avg `0.073` n `114`; fx avg `-0.0208` n `6`; index avg `-0.0235` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0713` n `793`
- 1h: commodity avg `-0.0158` n `12`; crypto_alt avg `0.0719` n `230`; crypto_major avg `0.2062` n `8`; equity avg `0.0762` n `114`; fx avg `-0.0041` n `6`; index avg `-0.049` n `25`; metal avg `0.0535` n `20`; unknown avg `-0.1238` n `793`
- 4h: commodity avg `0.0306` n `12`; crypto_alt avg `-0.1468` n `230`; crypto_major avg `0.3018` n `8`; equity avg `0.179` n `114`; fx avg `-0.0264` n `6`; index avg `-0.0411` n `25`; metal avg `0.0195` n `20`; unknown avg `-0.207` n `792`
- 24h: commodity avg `0.6132` n `12`; crypto_alt avg `0.3343` n `230`; crypto_major avg `1.5663` n `8`; equity avg `1.1361` n `114`; fx avg `-0.0104` n `6`; index avg `-0.0141` n `25`; metal avg `0.2145` n `20`; unknown avg `0.3704` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
