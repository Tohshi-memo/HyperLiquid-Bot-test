# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T05:22:29.914865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0325` n `13`; crypto_alt avg `0.2169` n `235`; crypto_major avg `0.234` n `8`; equity avg `0.1075` n `150`; fx avg `0.0018` n `6`; index avg `0.0051` n `26`; metal avg `0.0158` n `20`; unknown avg `-0.0347` n `1078`
- 1h: commodity avg `0.0351` n `13`; crypto_alt avg `0.1111` n `235`; crypto_major avg `0.0444` n `8`; equity avg `0.178` n `150`; fx avg `0.0012` n `6`; index avg `0.018` n `26`; metal avg `0.0356` n `20`; unknown avg `-0.2258` n `1074`
- 4h: commodity avg `-0.1638` n `13`; crypto_alt avg `1.4025` n `235`; crypto_major avg `0.9657` n `8`; equity avg `0.756` n `150`; fx avg `0.0098` n `6`; index avg `0.1139` n `26`; metal avg `0.1818` n `20`; unknown avg `1.298` n `1068`
- 24h: commodity avg `0.1024` n `13`; crypto_alt avg `-1.5049` n `235`; crypto_major avg `-2.2024` n `8`; equity avg `-1.6354` n `150`; fx avg `0.1089` n `6`; index avg `-0.1812` n `26`; metal avg `0.2139` n `20`; unknown avg `5.7612` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
