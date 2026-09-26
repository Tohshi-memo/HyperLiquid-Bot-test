# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T18:37:27.073766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `-0.2675` n `234`; crypto_major avg `-0.1522` n `8`; equity avg `-0.0087` n `141`; fx avg `0.0021` n `6`; index avg `0.0051` n `26`; metal avg `0.0004` n `20`; unknown avg `0.3058` n `961`
- 1h: commodity avg `0.0275` n `12`; crypto_alt avg `-0.4175` n `234`; crypto_major avg `-0.2203` n `8`; equity avg `-0.0383` n `141`; fx avg `-0.0008` n `6`; index avg `-0.0188` n `26`; metal avg `-0.0047` n `20`; unknown avg `-0.0484` n `959`
- 4h: commodity avg `-0.029` n `12`; crypto_alt avg `0.0239` n `234`; crypto_major avg `-0.2685` n `8`; equity avg `0.0137` n `141`; fx avg `-0.0096` n `6`; index avg `-0.0079` n `26`; metal avg `-0.0096` n `20`; unknown avg `10.4808` n `945`
- 24h: commodity avg `0.4053` n `12`; crypto_alt avg `1.8348` n `234`; crypto_major avg `-0.559` n `8`; equity avg `-0.0487` n `141`; fx avg `0.0196` n `6`; index avg `-0.0217` n `26`; metal avg `-0.0443` n `20`; unknown avg `3.4121` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
