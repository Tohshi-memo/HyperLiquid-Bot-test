# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T04:37:32.830572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `0.23` n `234`; crypto_major avg `0.2192` n `8`; equity avg `0.054` n `141`; fx avg `0.0039` n `6`; index avg `0.0112` n `26`; metal avg `0.013` n `20`; unknown avg `0.4758` n `946`
- 1h: commodity avg `0.0416` n `12`; crypto_alt avg `0.5364` n `234`; crypto_major avg `0.1609` n `8`; equity avg `-0.0042` n `141`; fx avg `0.003` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0291` n `20`; unknown avg `0.9706` n `938`
- 4h: commodity avg `-0.026` n `12`; crypto_alt avg `-0.409` n `234`; crypto_major avg `-0.3819` n `8`; equity avg `0.2673` n `141`; fx avg `-0.1229` n `6`; index avg `0.0826` n `26`; metal avg `-0.0243` n `20`; unknown avg `3.521` n `938`
- 24h: commodity avg `0.5266` n `12`; crypto_alt avg `2.5012` n `234`; crypto_major avg `1.0298` n `8`; equity avg `0.5275` n `141`; fx avg `-0.1317` n `6`; index avg `0.0353` n `26`; metal avg `-0.1861` n `20`; unknown avg `17.9381` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
