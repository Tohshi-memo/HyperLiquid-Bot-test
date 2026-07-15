# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T04:07:28.071373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0417` n `12`; crypto_alt avg `-0.0373` n `230`; crypto_major avg `-0.108` n `8`; equity avg `0.1395` n `93`; fx avg `-0.0046` n `6`; index avg `0.0` n `25`; metal avg `-0.0175` n `20`; unknown avg `-0.0921` n `767`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `0.3047` n `230`; crypto_major avg `0.2109` n `8`; equity avg `0.361` n `93`; fx avg `0.005` n `6`; index avg `0.0604` n `25`; metal avg `-0.0671` n `20`; unknown avg `0.0627` n `767`
- 4h: commodity avg `0.0199` n `12`; crypto_alt avg `-0.0217` n `230`; crypto_major avg `-0.0706` n `8`; equity avg `1.2543` n `93`; fx avg `0.0504` n `6`; index avg `0.1654` n `25`; metal avg `-0.1091` n `20`; unknown avg `-0.353` n `767`
- 24h: commodity avg `0.0945` n `12`; crypto_alt avg `2.0165` n `230`; crypto_major avg `3.3203` n `8`; equity avg `2.8841` n `92`; fx avg `0.142` n `6`; index avg `0.7659` n `25`; metal avg `0.3781` n `20`; unknown avg `0.281` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
