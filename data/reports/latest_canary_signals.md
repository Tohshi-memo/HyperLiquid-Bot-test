# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T12:37:33.584929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `0.0818` n `230`; crypto_major avg `0.0881` n `8`; equity avg `-0.157` n `107`; fx avg `0.0148` n `6`; index avg `-0.0336` n `25`; metal avg `0.1871` n `20`; unknown avg `-0.0783` n `781`
- 1h: commodity avg `-0.4495` n `12`; crypto_alt avg `0.1252` n `230`; crypto_major avg `0.3381` n `8`; equity avg `0.0963` n `107`; fx avg `-0.0125` n `6`; index avg `0.0227` n `25`; metal avg `0.2915` n `20`; unknown avg `-0.0801` n `781`
- 4h: commodity avg `-0.9215` n `12`; crypto_alt avg `-0.025` n `230`; crypto_major avg `0.6461` n `8`; equity avg `0.6167` n `107`; fx avg `-0.0583` n `6`; index avg `0.1196` n `25`; metal avg `0.5401` n `20`; unknown avg `0.13` n `781`
- 24h: commodity avg `-0.5348` n `12`; crypto_alt avg `1.0279` n `230`; crypto_major avg `1.802` n `8`; equity avg `5.0928` n `107`; fx avg `0.0494` n `6`; index avg `0.6187` n `25`; metal avg `1.0248` n `20`; unknown avg `0.9185` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
