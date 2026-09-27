# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T02:22:29.660332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `12`; crypto_alt avg `0.0393` n `234`; crypto_major avg `0.0798` n `8`; equity avg `0.0347` n `141`; fx avg `-0.0102` n `6`; index avg `0.0003` n `26`; metal avg `0.0011` n `20`; unknown avg `3.1167` n `961`
- 1h: commodity avg `0.0016` n `12`; crypto_alt avg `0.4852` n `234`; crypto_major avg `0.3404` n `8`; equity avg `0.0425` n `141`; fx avg `-0.0062` n `6`; index avg `-0.0026` n `26`; metal avg `0.0024` n `20`; unknown avg `2.0695` n `959`
- 4h: commodity avg `-0.082` n `12`; crypto_alt avg `0.3623` n `234`; crypto_major avg `0.4157` n `8`; equity avg `0.1101` n `141`; fx avg `-0.0036` n `6`; index avg `-0.0003` n `26`; metal avg `0.002` n `20`; unknown avg `0.4695` n `951`
- 24h: commodity avg `-0.0454` n `12`; crypto_alt avg `0.8058` n `234`; crypto_major avg `-0.4485` n `8`; equity avg `0.2192` n `141`; fx avg `0.0146` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0104` n `20`; unknown avg `4.1618` n `885`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
