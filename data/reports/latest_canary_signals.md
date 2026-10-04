# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T17:07:30.279136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `13`; crypto_alt avg `0.0147` n `235`; crypto_major avg `0.0097` n `8`; equity avg `-0.0027` n `144`; fx avg `-0.0032` n `6`; index avg `-0.0012` n `26`; metal avg `0.0007` n `20`; unknown avg `0.039` n `1076`
- 1h: commodity avg `-0.0292` n `13`; crypto_alt avg `0.1472` n `235`; crypto_major avg `0.2429` n `8`; equity avg `0.0302` n `144`; fx avg `-0.0098` n `6`; index avg `-0.0006` n `26`; metal avg `0.0035` n `20`; unknown avg `1.2501` n `1076`
- 4h: commodity avg `-0.0708` n `13`; crypto_alt avg `0.0616` n `235`; crypto_major avg `0.2913` n `8`; equity avg `0.0368` n `144`; fx avg `0.003` n `6`; index avg `-0.0176` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.0281` n `1070`
- 24h: commodity avg `-0.1053` n `13`; crypto_alt avg `0.8121` n `235`; crypto_major avg `0.9103` n `8`; equity avg `0.2239` n `144`; fx avg `0.0139` n `6`; index avg `-0.0127` n `26`; metal avg `-0.0071` n `20`; unknown avg `-0.0626` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2033`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
