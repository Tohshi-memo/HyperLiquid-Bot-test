# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T01:37:30.546703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.1022` n `230`; crypto_major avg `-0.0115` n `8`; equity avg `-0.051` n `102`; fx avg `0.0003` n `6`; index avg `0.0178` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.0257` n `781`
- 1h: commodity avg `-0.0503` n `12`; crypto_alt avg `0.2375` n `230`; crypto_major avg `0.1434` n `8`; equity avg `0.008` n `102`; fx avg `-0.0008` n `6`; index avg `0.018` n `25`; metal avg `-0.0056` n `20`; unknown avg `-0.176` n `781`
- 4h: commodity avg `-0.2339` n `12`; crypto_alt avg `0.6948` n `230`; crypto_major avg `0.1539` n `8`; equity avg `-0.1241` n `102`; fx avg `-0.0224` n `6`; index avg `0.0081` n `25`; metal avg `-0.0065` n `20`; unknown avg `6.6017` n `781`
- 24h: commodity avg `0.9144` n `12`; crypto_alt avg `-0.3331` n `230`; crypto_major avg `-2.1458` n `8`; equity avg `-2.5562` n `102`; fx avg `-0.126` n `6`; index avg `-0.2803` n `25`; metal avg `-0.2151` n `20`; unknown avg `2.6387` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
