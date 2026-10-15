# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T10:47:24.047578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `13`; crypto_alt avg `-0.193` n `236`; crypto_major avg `-0.2286` n `8`; equity avg `-0.1682` n `151`; fx avg `0.0024` n `6`; index avg `-0.0238` n `26`; metal avg `0.0007` n `20`; unknown avg `-0.1554` n `1136`
- 1h: commodity avg `0.1033` n `13`; crypto_alt avg `-0.5826` n `236`; crypto_major avg `-0.6404` n `8`; equity avg `-0.2859` n `151`; fx avg `-0.0168` n `6`; index avg `-0.0185` n `26`; metal avg `-0.0491` n `20`; unknown avg `-0.1079` n `1062`
- 4h: commodity avg `0.036` n `13`; crypto_alt avg `0.0545` n `236`; crypto_major avg `0.0414` n `8`; equity avg `-0.3925` n `151`; fx avg `0.0203` n `6`; index avg `0.0121` n `26`; metal avg `0.2497` n `20`; unknown avg `4.4718` n `1038`
- 24h: commodity avg `-0.3761` n `13`; crypto_alt avg `-4.7577` n `236`; crypto_major avg `-3.6619` n `8`; equity avg `-6.0615` n `151`; fx avg `0.0518` n `6`; index avg `-0.9546` n `26`; metal avg `-0.3992` n `20`; unknown avg `2.2992` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1222`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1052`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0887`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0864`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0772`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
