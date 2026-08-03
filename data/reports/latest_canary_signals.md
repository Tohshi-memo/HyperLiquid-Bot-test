# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T01:22:32.962426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.1821` n `230`; crypto_major avg `-0.1639` n `8`; equity avg `-0.1692` n `102`; fx avg `0.0299` n `6`; index avg `-0.0247` n `25`; metal avg `-0.0377` n `20`; unknown avg `0.1187` n `784`
- 1h: commodity avg `0.0384` n `12`; crypto_alt avg `-0.3941` n `230`; crypto_major avg `-0.3481` n `8`; equity avg `-0.004` n `102`; fx avg `-0.2206` n `6`; index avg `-0.0242` n `25`; metal avg `-0.0681` n `20`; unknown avg `0.0306` n `784`
- 4h: commodity avg `-0.0463` n `12`; crypto_alt avg `-0.7238` n `230`; crypto_major avg `-0.6721` n `8`; equity avg `0.2152` n `102`; fx avg `-0.2979` n `6`; index avg `-0.1135` n `25`; metal avg `-0.2881` n `20`; unknown avg `2.1443` n `783`
- 24h: commodity avg `-0.9262` n `12`; crypto_alt avg `0.0317` n `230`; crypto_major avg `0.6183` n `8`; equity avg `1.409` n `102`; fx avg `-0.2799` n `6`; index avg `0.1612` n `25`; metal avg `0.0345` n `20`; unknown avg `1.473` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
