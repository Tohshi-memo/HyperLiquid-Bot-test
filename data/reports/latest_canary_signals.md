# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T16:07:26.647508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `13`; crypto_alt avg `0.0356` n `235`; crypto_major avg `-0.0855` n `8`; equity avg `0.0082` n `143`; fx avg `0.0093` n `6`; index avg `0.0034` n `26`; metal avg `0.0098` n `20`; unknown avg `0.4226` n `1070`
- 1h: commodity avg `0.0829` n `13`; crypto_alt avg `0.1099` n `235`; crypto_major avg `-0.0115` n `8`; equity avg `0.0322` n `143`; fx avg `0.0041` n `6`; index avg `0.0114` n `26`; metal avg `0.0122` n `20`; unknown avg `-0.0712` n `1038`
- 4h: commodity avg `0.24` n `13`; crypto_alt avg `0.5573` n `235`; crypto_major avg `0.2432` n `8`; equity avg `0.0379` n `143`; fx avg `-0.0098` n `6`; index avg `0.021` n `26`; metal avg `0.0076` n `20`; unknown avg `0.2035` n `950`
- 24h: commodity avg `0.5787` n `13`; crypto_alt avg `-1.2519` n `235`; crypto_major avg `-0.7258` n `8`; equity avg `-0.0495` n `143`; fx avg `-0.0351` n `6`; index avg `0.0186` n `26`; metal avg `0.1617` n `20`; unknown avg `0.0562` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1967`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
