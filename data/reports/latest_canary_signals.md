# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T02:52:38.235139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `13`; crypto_alt avg `-0.0627` n `235`; crypto_major avg `-0.0663` n `8`; equity avg `-0.0193` n `143`; fx avg `0.0104` n `6`; index avg `-0.003` n `26`; metal avg `-0.0098` n `20`; unknown avg `-0.1267` n `984`
- 1h: commodity avg `-0.0315` n `13`; crypto_alt avg `0.1074` n `235`; crypto_major avg `-0.1202` n `8`; equity avg `0.0122` n `143`; fx avg `0.0075` n `6`; index avg `0.0083` n `26`; metal avg `0.0102` n `20`; unknown avg `-0.1001` n `982`
- 4h: commodity avg `-0.2485` n `13`; crypto_alt avg `0.9544` n `235`; crypto_major avg `0.4425` n `8`; equity avg `0.0781` n `143`; fx avg `0.0251` n `6`; index avg `0.0293` n `26`; metal avg `-0.0224` n `20`; unknown avg `-0.0298` n `976`
- 24h: commodity avg `0.0514` n `13`; crypto_alt avg `-0.7617` n `235`; crypto_major avg `-0.7071` n `8`; equity avg `0.6707` n `142`; fx avg `-0.1061` n `6`; index avg `0.2751` n `26`; metal avg `-0.1619` n `20`; unknown avg `-0.7485` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
