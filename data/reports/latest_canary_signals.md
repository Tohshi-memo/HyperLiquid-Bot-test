# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T07:37:28.498665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0198` n `12`; crypto_alt avg `0.0438` n `234`; crypto_major avg `-0.0338` n `8`; equity avg `0.0029` n `141`; fx avg `0.0133` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0024` n `20`; unknown avg `-0.0666` n `961`
- 1h: commodity avg `-0.0248` n `12`; crypto_alt avg `0.4207` n `234`; crypto_major avg `0.1702` n `8`; equity avg `0.0332` n `141`; fx avg `0.0294` n `6`; index avg `-0.0025` n `26`; metal avg `-0.0068` n `20`; unknown avg `0.0787` n `959`
- 4h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.7095` n `234`; crypto_major avg `-0.276` n `8`; equity avg `0.0294` n `141`; fx avg `0.0133` n `6`; index avg `-0.0087` n `26`; metal avg `-0.005` n `20`; unknown avg `0.8659` n `929`
- 24h: commodity avg `-0.006` n `12`; crypto_alt avg `3.7667` n `234`; crypto_major avg `1.1197` n `8`; equity avg `-0.612` n `141`; fx avg `-0.0786` n `6`; index avg `0.0571` n `26`; metal avg `0.2278` n `20`; unknown avg `1125.9102` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
