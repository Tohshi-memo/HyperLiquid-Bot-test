# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T06:37:31.450254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0733` n `12`; crypto_alt avg `0.1112` n `234`; crypto_major avg `0.0762` n `8`; equity avg `-0.0645` n `141`; fx avg `-0.0065` n `6`; index avg `-0.0196` n `26`; metal avg `-0.0483` n `20`; unknown avg `0.5008` n `945`
- 1h: commodity avg `0.1367` n `12`; crypto_alt avg `-0.0721` n `234`; crypto_major avg `-0.0122` n `8`; equity avg `-0.3897` n `141`; fx avg `0.0177` n `6`; index avg `-0.073` n `26`; metal avg `-0.0638` n `20`; unknown avg `0.5934` n `927`
- 4h: commodity avg `0.272` n `12`; crypto_alt avg `0.9537` n `234`; crypto_major avg `0.369` n `8`; equity avg `-0.5214` n `141`; fx avg `0.0189` n `6`; index avg `-0.1085` n `26`; metal avg `-0.0552` n `20`; unknown avg `1.975` n `921`
- 24h: commodity avg `0.757` n `12`; crypto_alt avg `-4.1938` n `234`; crypto_major avg `-3.8919` n `8`; equity avg `-2.2595` n `140`; fx avg `0.0415` n `6`; index avg `-0.4737` n `26`; metal avg `-0.5895` n `20`; unknown avg `586.3194` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
