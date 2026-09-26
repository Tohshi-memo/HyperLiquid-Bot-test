# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T10:07:29.010717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `0.1988` n `234`; crypto_major avg `0.1514` n `8`; equity avg `0.0174` n `141`; fx avg `-0.0006` n `6`; index avg `0.0029` n `26`; metal avg `-0.0008` n `20`; unknown avg `3.2972` n `959`
- 1h: commodity avg `-0.0021` n `12`; crypto_alt avg `0.0219` n `234`; crypto_major avg `-0.1649` n `8`; equity avg `-0.0479` n `141`; fx avg `-0.0008` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0087` n `20`; unknown avg `2.2153` n `959`
- 4h: commodity avg `-0.0554` n `12`; crypto_alt avg `0.7571` n `234`; crypto_major avg `-0.0331` n `8`; equity avg `0.0117` n `141`; fx avg `0.0214` n `6`; index avg `0.0007` n `26`; metal avg `-0.0103` n `20`; unknown avg `2.8328` n `943`
- 24h: commodity avg `0.0792` n `12`; crypto_alt avg `2.3612` n `234`; crypto_major avg `0.0118` n `8`; equity avg `-0.8301` n `141`; fx avg `-0.0522` n `6`; index avg `0.0126` n `26`; metal avg `-0.004` n `20`; unknown avg `1122.718` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
