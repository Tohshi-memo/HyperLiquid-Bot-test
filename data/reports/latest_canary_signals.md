# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T08:37:24.520533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.0644` n `230`; crypto_major avg `-0.0204` n `8`; equity avg `-0.0269` n `102`; fx avg `0.0007` n `6`; index avg `0.0031` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.0046` n `781`
- 1h: commodity avg `0.0424` n `12`; crypto_alt avg `0.0743` n `230`; crypto_major avg `0.0844` n `8`; equity avg `0.1122` n `102`; fx avg `0.0162` n `6`; index avg `0.0086` n `25`; metal avg `-0.0287` n `20`; unknown avg `-0.0493` n `781`
- 4h: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.1904` n `230`; crypto_major avg `-0.1735` n `8`; equity avg `0.0922` n `102`; fx avg `0.0213` n `6`; index avg `-0.0088` n `25`; metal avg `0.035` n `20`; unknown avg `0.0004` n `765`
- 24h: commodity avg `0.8678` n `12`; crypto_alt avg `0.0847` n `230`; crypto_major avg `-1.3227` n `8`; equity avg `-2.5807` n `102`; fx avg `0.0017` n `6`; index avg `-0.2727` n `25`; metal avg `-0.111` n `20`; unknown avg `4.843` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
