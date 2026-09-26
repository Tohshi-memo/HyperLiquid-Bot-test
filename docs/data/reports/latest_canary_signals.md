# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T11:37:32.520701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `-0.0136` n `234`; crypto_major avg `0.1144` n `8`; equity avg `0.0217` n `141`; fx avg `0.0279` n `6`; index avg `0.0003` n `26`; metal avg `0.0001` n `20`; unknown avg `-0.0395` n `961`
- 1h: commodity avg `-0.0357` n `12`; crypto_alt avg `0.2332` n `234`; crypto_major avg `0.1707` n `8`; equity avg `0.0432` n `141`; fx avg `0.0258` n `6`; index avg `0.0038` n `26`; metal avg `-0.0011` n `20`; unknown avg `2.2669` n `959`
- 4h: commodity avg `-0.0471` n `12`; crypto_alt avg `0.5724` n `234`; crypto_major avg `0.1877` n `8`; equity avg `0.0642` n `141`; fx avg `0.0243` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0049` n `20`; unknown avg `1.6749` n `943`
- 24h: commodity avg `0.2342` n `12`; crypto_alt avg `1.6866` n `234`; crypto_major avg `-0.8666` n `8`; equity avg `-0.8908` n `141`; fx avg `-0.0179` n `6`; index avg `-0.0227` n `26`; metal avg `-0.0384` n `20`; unknown avg `1121.8434` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
