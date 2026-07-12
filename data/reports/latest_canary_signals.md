# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T18:22:29.274091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.009` n `230`; crypto_major avg `-0.0588` n `8`; equity avg `0.0106` n `92`; fx avg `-0.0103` n `6`; index avg `0.0276` n `25`; metal avg `0.0045` n `20`; unknown avg `0.0211` n `765`
- 1h: commodity avg `0.0718` n `12`; crypto_alt avg `-0.115` n `230`; crypto_major avg `-0.1469` n `8`; equity avg `-0.0267` n `92`; fx avg `-0.025` n `6`; index avg `0.0118` n `25`; metal avg `0.0053` n `20`; unknown avg `0.0074` n `765`
- 4h: commodity avg `0.1662` n `12`; crypto_alt avg `0.0884` n `230`; crypto_major avg `0.2826` n `8`; equity avg `-0.0192` n `92`; fx avg `-0.0292` n `6`; index avg `0.0441` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0878` n `759`
- 24h: commodity avg `0.6112` n `12`; crypto_alt avg `-1.5544` n `230`; crypto_major avg `-0.7419` n `8`; equity avg `-0.2609` n `92`; fx avg `-0.0078` n `6`; index avg `-0.0847` n `25`; metal avg `-0.0975` n `20`; unknown avg `0.1222` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
