# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T17:52:26.892788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.1738` n `230`; crypto_major avg `-0.0732` n `8`; equity avg `-0.0267` n `92`; fx avg `0.1012` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0065` n `765`
- 1h: commodity avg `0.0114` n `12`; crypto_alt avg `-0.1271` n `230`; crypto_major avg `-0.0957` n `8`; equity avg `-0.0201` n `92`; fx avg `0.0952` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0076` n `20`; unknown avg `0.0037` n `765`
- 4h: commodity avg `0.078` n `12`; crypto_alt avg `0.0266` n `230`; crypto_major avg `0.3608` n `8`; equity avg `-0.0339` n `92`; fx avg `0.0961` n `6`; index avg `0.0229` n `25`; metal avg `-0.0242` n `20`; unknown avg `-0.0802` n `759`
- 24h: commodity avg `0.5288` n `12`; crypto_alt avg `-1.3283` n `230`; crypto_major avg `-0.5324` n `8`; equity avg `-0.205` n `92`; fx avg `0.1124` n `6`; index avg `-0.0905` n `25`; metal avg `-0.1082` n `20`; unknown avg `0.1567` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
