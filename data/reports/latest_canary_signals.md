# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T02:22:27.735591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `0.0865` n `230`; crypto_major avg `0.0918` n `8`; equity avg `0.1832` n `114`; fx avg `0.0035` n `6`; index avg `0.0126` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0299` n `792`
- 1h: commodity avg `0.1411` n `12`; crypto_alt avg `-0.0076` n `230`; crypto_major avg `0.0488` n `8`; equity avg `0.0278` n `114`; fx avg `0.0121` n `6`; index avg `-0.0003` n `25`; metal avg `-0.09` n `20`; unknown avg `-0.1217` n `792`
- 4h: commodity avg `0.0158` n `12`; crypto_alt avg `0.4196` n `230`; crypto_major avg `0.6141` n `8`; equity avg `0.2592` n `114`; fx avg `-0.043` n `6`; index avg `0.002` n `25`; metal avg `0.2315` n `20`; unknown avg `0.0823` n `791`
- 24h: commodity avg `-0.0904` n `12`; crypto_alt avg `0.0181` n `230`; crypto_major avg `0.2273` n `8`; equity avg `0.5158` n `114`; fx avg `-0.0527` n `6`; index avg `0.0489` n `25`; metal avg `0.227` n `20`; unknown avg `-0.0574` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
