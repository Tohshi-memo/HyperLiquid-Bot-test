# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T13:52:26.481148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.045` n `12`; crypto_alt avg `-0.1411` n `230`; crypto_major avg `-0.0985` n `8`; equity avg `0.0065` n `92`; fx avg `0.002` n `6`; index avg `-0.008` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0046` n `765`
- 1h: commodity avg `0.0604` n `12`; crypto_alt avg `-0.0127` n `230`; crypto_major avg `0.0794` n `8`; equity avg `0.021` n `92`; fx avg `0.0034` n `6`; index avg `0.0227` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.0431` n `765`
- 4h: commodity avg `-0.0247` n `12`; crypto_alt avg `-0.0469` n `230`; crypto_major avg `0.2969` n `8`; equity avg `0.0823` n `92`; fx avg `0.003` n `6`; index avg `0.0243` n `25`; metal avg `-0.0057` n `20`; unknown avg `-0.0846` n `763`
- 24h: commodity avg `0.4775` n `12`; crypto_alt avg `-1.1429` n `230`; crypto_major avg `-0.492` n `8`; equity avg `-0.0414` n `92`; fx avg `0.0125` n `6`; index avg `-0.0935` n `25`; metal avg `-0.1089` n `20`; unknown avg `0.0969` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
