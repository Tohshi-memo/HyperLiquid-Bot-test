# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T21:07:35.874322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `-0.1578` n `234`; crypto_major avg `-0.1923` n `8`; equity avg `-0.0016` n `141`; fx avg `-0.0021` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0055` n `20`; unknown avg `0.939` n `942`
- 1h: commodity avg `-0.1063` n `12`; crypto_alt avg `-0.3175` n `234`; crypto_major avg `-0.3108` n `8`; equity avg `0.0207` n `141`; fx avg `-0.0128` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0336` n `20`; unknown avg `4.2758` n `906`
- 4h: commodity avg `0.0851` n `12`; crypto_alt avg `-0.0846` n `234`; crypto_major avg `-0.1002` n `8`; equity avg `-0.3522` n `141`; fx avg `-0.0101` n `6`; index avg `-0.0999` n `26`; metal avg `-0.0413` n `20`; unknown avg `8.3711` n `869`
- 24h: commodity avg `0.7293` n `12`; crypto_alt avg `4.1151` n `234`; crypto_major avg `1.4974` n `8`; equity avg `-0.2703` n `141`; fx avg `0.04` n `6`; index avg `-0.1203` n `26`; metal avg `-0.1217` n `20`; unknown avg `13.4368` n `849`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
