# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T12:22:37.990784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0433` n `13`; crypto_alt avg `-0.0144` n `236`; crypto_major avg `0.1059` n `8`; equity avg `-0.0664` n `151`; fx avg `-0.0019` n `6`; index avg `-0.003` n `26`; metal avg `0.0036` n `20`; unknown avg `0.1153` n `1136`
- 1h: commodity avg `0.0246` n `13`; crypto_alt avg `0.02` n `236`; crypto_major avg `0.0173` n `8`; equity avg `-0.0404` n `151`; fx avg `0.0043` n `6`; index avg `0.0054` n `26`; metal avg `-0.0471` n `20`; unknown avg `0.6595` n `1128`
- 4h: commodity avg `0.1392` n `13`; crypto_alt avg `-0.1915` n `236`; crypto_major avg `-0.3661` n `8`; equity avg `-0.0858` n `151`; fx avg `0.0074` n `6`; index avg `0.0114` n `26`; metal avg `-0.0009` n `20`; unknown avg `-0.0177` n `1048`
- 24h: commodity avg `-0.2685` n `13`; crypto_alt avg `-4.7308` n `236`; crypto_major avg `-3.7577` n `8`; equity avg `-6.1417` n `151`; fx avg `0.0598` n `6`; index avg `-0.9921` n `26`; metal avg `-0.5149` n `20`; unknown avg `2.9768` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1219`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1058`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0676`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
