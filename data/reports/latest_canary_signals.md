# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T18:52:27.361530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `0.1881` n `234`; crypto_major avg `0.0618` n `8`; equity avg `0.002` n `141`; fx avg `0.0012` n `6`; index avg `0.0006` n `26`; metal avg `0.0021` n `20`; unknown avg `11.441` n `962`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `0.526` n `234`; crypto_major avg `0.4168` n `8`; equity avg `0.0327` n `141`; fx avg `-0.0007` n `6`; index avg `0.0049` n `26`; metal avg `0.0039` n `20`; unknown avg `13.7892` n `960`
- 4h: commodity avg `-0.1049` n `12`; crypto_alt avg `1.1868` n `234`; crypto_major avg `0.5655` n `8`; equity avg `0.1715` n `141`; fx avg `0.0095` n `6`; index avg `0.0343` n `26`; metal avg `0.0124` n `20`; unknown avg `8.2906` n `954`
- 24h: commodity avg `-0.114` n `12`; crypto_alt avg `0.9022` n `234`; crypto_major avg `0.79` n `8`; equity avg `0.4024` n `141`; fx avg `-0.0204` n `6`; index avg `0.0396` n `26`; metal avg `-0.0027` n `20`; unknown avg `118.4272` n `897`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
