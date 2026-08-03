# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T07:38:09.014183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.068` n `12`; crypto_alt avg `0.0065` n `230`; crypto_major avg `0.015` n `8`; equity avg `-0.0498` n `102`; fx avg `-0.0117` n `6`; index avg `0.0088` n `25`; metal avg `0.0486` n `20`; unknown avg `0.0017` n `784`
- 1h: commodity avg `0.1339` n `12`; crypto_alt avg `-0.1107` n `230`; crypto_major avg `-0.1479` n `8`; equity avg `-0.2408` n `102`; fx avg `-0.0466` n `6`; index avg `-0.0141` n `25`; metal avg `-0.0777` n `20`; unknown avg `-0.0193` n `784`
- 4h: commodity avg `0.0378` n `12`; crypto_alt avg `-0.2358` n `230`; crypto_major avg `-0.4211` n `8`; equity avg `-0.3101` n `102`; fx avg `-0.0132` n `6`; index avg `-0.02` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0064` n `768`
- 24h: commodity avg `-0.1242` n `12`; crypto_alt avg `-1.1953` n `230`; crypto_major avg `-0.8679` n `8`; equity avg `0.5203` n `102`; fx avg `-0.1864` n `6`; index avg `-0.031` n `25`; metal avg `-0.1188` n `20`; unknown avg `0.9423` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
