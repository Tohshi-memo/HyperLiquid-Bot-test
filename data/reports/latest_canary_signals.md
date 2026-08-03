# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T15:37:40.932208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `0.0331` n `230`; crypto_major avg `0.0883` n `8`; equity avg `-0.1203` n `103`; fx avg `-0.016` n `6`; index avg `0.0089` n `25`; metal avg `-0.0386` n `20`; unknown avg `-0.1465` n `784`
- 1h: commodity avg `0.0504` n `12`; crypto_alt avg `-0.011` n `230`; crypto_major avg `0.1339` n `8`; equity avg `0.0509` n `103`; fx avg `0.0147` n `6`; index avg `0.0168` n `25`; metal avg `0.0178` n `20`; unknown avg `-0.2707` n `784`
- 4h: commodity avg `0.0172` n `12`; crypto_alt avg `0.8849` n `230`; crypto_major avg `1.19` n `8`; equity avg `1.9217` n `103`; fx avg `-0.0603` n `6`; index avg `0.114` n `25`; metal avg `-0.2193` n `20`; unknown avg `-0.0978` n `784`
- 24h: commodity avg `-0.2464` n `12`; crypto_alt avg `0.1349` n `230`; crypto_major avg `1.0648` n `8`; equity avg `1.1745` n `102`; fx avg `-0.1987` n `6`; index avg `-0.0315` n `25`; metal avg `-0.4782` n `20`; unknown avg `0.0306` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
