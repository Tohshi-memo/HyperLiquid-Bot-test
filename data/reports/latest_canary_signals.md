# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T15:07:27.556291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `13`; crypto_alt avg `0.6223` n `239`; crypto_major avg `0.9494` n `8`; equity avg `1.151` n `168`; fx avg `0.006` n `6`; index avg `0.1452` n `27`; metal avg `0.1648` n `20`; unknown avg `43.3919` n `1255`
- 1h: commodity avg `0.2648` n `13`; crypto_alt avg `0.1854` n `239`; crypto_major avg `0.3962` n `8`; equity avg `-0.2597` n `168`; fx avg `-0.0192` n `6`; index avg `-0.0146` n `27`; metal avg `-0.1392` n `20`; unknown avg `241.5893` n `1247`
- 4h: commodity avg `0.4274` n `13`; crypto_alt avg `-1.2877` n `239`; crypto_major avg `-0.9653` n `8`; equity avg `-1.5534` n `168`; fx avg `0.0164` n `6`; index avg `-0.1372` n `27`; metal avg `-0.446` n `20`; unknown avg `249.3116` n `1207`
- 24h: commodity avg `0.3251` n `13`; crypto_alt avg `-2.0` n `239`; crypto_major avg `-2.6653` n `8`; equity avg `-5.0495` n `168`; fx avg `-0.061` n `6`; index avg `-0.4816` n `27`; metal avg `-1.2785` n `20`; unknown avg `615.8013` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
