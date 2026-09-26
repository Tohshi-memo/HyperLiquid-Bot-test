# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T22:07:30.152087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `0.2654` n `234`; crypto_major avg `0.1764` n `8`; equity avg `0.0307` n `141`; fx avg `-0.0029` n `6`; index avg `0.0001` n `26`; metal avg `0.0009` n `20`; unknown avg `1.3388` n `935`
- 1h: commodity avg `0.024` n `12`; crypto_alt avg `0.6163` n `234`; crypto_major avg `0.443` n `8`; equity avg `0.0516` n `141`; fx avg `0.0008` n `6`; index avg `0.0024` n `26`; metal avg `0.0042` n `20`; unknown avg `1.7368` n `935`
- 4h: commodity avg `0.0526` n `12`; crypto_alt avg `-0.8076` n `234`; crypto_major avg `-0.1273` n `8`; equity avg `-0.0193` n `141`; fx avg `-0.0159` n `6`; index avg `-0.0181` n `26`; metal avg `0.0063` n `20`; unknown avg `129.0469` n `929`
- 24h: commodity avg `0.3174` n `12`; crypto_alt avg `1.4124` n `234`; crypto_major avg `-0.3107` n `8`; equity avg `-0.0118` n `141`; fx avg `0.024` n `6`; index avg `-0.0569` n `26`; metal avg `-0.0172` n `20`; unknown avg `4.9189` n `868`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
