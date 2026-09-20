# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T21:22:23.772255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `-0.1162` n `234`; crypto_major avg `-0.1999` n `8`; equity avg `-0.0425` n `140`; fx avg `-0.0449` n `6`; index avg `-0.0065` n `26`; metal avg `-0.0276` n `20`; unknown avg `31.6139` n `931`
- 1h: commodity avg `0.0071` n `12`; crypto_alt avg `-0.4938` n `234`; crypto_major avg `-0.5047` n `8`; equity avg `-0.0095` n `140`; fx avg `-0.0245` n `6`; index avg `0.0252` n `26`; metal avg `-0.0278` n `20`; unknown avg `2.4939` n `893`
- 4h: commodity avg `0.0158` n `12`; crypto_alt avg `-0.0851` n `234`; crypto_major avg `-0.3407` n `8`; equity avg `-0.0138` n `140`; fx avg `-0.0551` n `6`; index avg `0.0138` n `26`; metal avg `-0.0537` n `20`; unknown avg `1.1335` n `879`
- 24h: commodity avg `0.3439` n `12`; crypto_alt avg `0.8758` n `234`; crypto_major avg `-0.3582` n `8`; equity avg `-0.1113` n `140`; fx avg `-0.0322` n `6`; index avg `-0.0322` n `26`; metal avg `-0.0729` n `20`; unknown avg `2.4599` n `779`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
