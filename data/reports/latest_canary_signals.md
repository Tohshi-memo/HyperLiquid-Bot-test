# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T17:39:31.822964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `0.1145` n `230`; crypto_major avg `0.078` n `8`; equity avg `0.0066` n `92`; fx avg `-0.006` n `6`; index avg `0.0019` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0059` n `765`
- 1h: commodity avg `0.0553` n `12`; crypto_alt avg `0.0881` n `230`; crypto_major avg `0.06` n `8`; equity avg `0.0195` n `92`; fx avg `-0.0066` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.1015` n `765`
- 4h: commodity avg `0.1265` n `12`; crypto_alt avg `0.0586` n `230`; crypto_major avg `0.3353` n `8`; equity avg `-0.0008` n `92`; fx avg `-0.0032` n `6`; index avg `0.0164` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.0892` n `759`
- 24h: commodity avg `0.5694` n `12`; crypto_alt avg `-1.236` n `230`; crypto_major avg `-0.4903` n `8`; equity avg `-0.1539` n `92`; fx avg `0.0105` n `6`; index avg `-0.087` n `25`; metal avg `-0.1077` n `20`; unknown avg `0.1614` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
