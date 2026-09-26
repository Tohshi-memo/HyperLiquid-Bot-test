# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T10:52:29.953571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0278` n `12`; crypto_alt avg `0.1107` n `234`; crypto_major avg `0.0939` n `8`; equity avg `0.0106` n `141`; fx avg `-0.0013` n `6`; index avg `0.0025` n `26`; metal avg `0.0` n `20`; unknown avg `1.4656` n `961`
- 1h: commodity avg `0.0078` n `12`; crypto_alt avg `0.6545` n `234`; crypto_major avg `0.4018` n `8`; equity avg `0.0528` n `141`; fx avg `0.0027` n `6`; index avg `-0.0005` n `26`; metal avg `0.0043` n `20`; unknown avg `1.683` n `959`
- 4h: commodity avg `-0.0591` n `12`; crypto_alt avg `0.7986` n `234`; crypto_major avg `0.2003` n `8`; equity avg `0.0425` n `141`; fx avg `0.0126` n `6`; index avg `-0.0049` n `26`; metal avg `-0.0104` n `20`; unknown avg `0.1088` n `943`
- 24h: commodity avg `0.0589` n `12`; crypto_alt avg `2.3533` n `234`; crypto_major avg `-0.3415` n `8`; equity avg `-0.8663` n `141`; fx avg `-0.0394` n `6`; index avg `0.0216` n `26`; metal avg `-0.1163` n `20`; unknown avg `1121.0396` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
