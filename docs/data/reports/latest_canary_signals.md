# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T01:07:28.031758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0283` n `12`; crypto_alt avg `0.4243` n `230`; crypto_major avg `0.5468` n `8`; equity avg `0.1331` n `114`; fx avg `-0.0191` n `6`; index avg `0.0185` n `25`; metal avg `0.1127` n `20`; unknown avg `0.4016` n `792`
- 1h: commodity avg `-0.031` n `12`; crypto_alt avg `0.2791` n `230`; crypto_major avg `0.4989` n `8`; equity avg `0.1284` n `114`; fx avg `-0.0626` n `6`; index avg `-0.0126` n `25`; metal avg `0.2257` n `20`; unknown avg `0.2416` n `792`
- 4h: commodity avg `-0.2402` n `12`; crypto_alt avg `-0.0921` n `230`; crypto_major avg `0.104` n `8`; equity avg `0.1538` n `114`; fx avg `-0.0658` n `6`; index avg `0.0251` n `25`; metal avg `0.2505` n `20`; unknown avg `-0.1897` n `791`
- 24h: commodity avg `-0.1686` n `12`; crypto_alt avg `-0.2423` n `230`; crypto_major avg `0.1194` n `8`; equity avg `0.4625` n `114`; fx avg `-0.0676` n `6`; index avg `0.0477` n `25`; metal avg `0.2771` n `20`; unknown avg `0.0463` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
