# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T20:37:30.049687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `-0.1831` n `234`; crypto_major avg `-0.0412` n `8`; equity avg `-0.0087` n `141`; fx avg `-0.0114` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.6159` n `962`
- 1h: commodity avg `0.0635` n `12`; crypto_alt avg `-0.2142` n `234`; crypto_major avg `-0.1622` n `8`; equity avg `0.0076` n `141`; fx avg `-0.0114` n `6`; index avg `0.003` n `26`; metal avg `-0.0059` n `20`; unknown avg `11.2119` n `954`
- 4h: commodity avg `0.0491` n `12`; crypto_alt avg `0.6571` n `234`; crypto_major avg `0.3755` n `8`; equity avg `0.1459` n `141`; fx avg `-0.017` n `6`; index avg `0.0111` n `26`; metal avg `0.003` n `20`; unknown avg `3.0318` n `928`
- 24h: commodity avg `-0.1068` n `12`; crypto_alt avg `1.0942` n `234`; crypto_major avg `0.5371` n `8`; equity avg `0.3936` n `141`; fx avg `-0.028` n `6`; index avg `0.0442` n `26`; metal avg `-0.0146` n `20`; unknown avg `7.5052` n `871`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
