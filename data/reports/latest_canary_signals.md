# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T22:22:32.467053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `0.0646` n `234`; crypto_major avg `0.0772` n `8`; equity avg `-0.0462` n `141`; fx avg `0.008` n `6`; index avg `-0.0369` n `26`; metal avg `-0.0307` n `20`; unknown avg `0.6729` n `948`
- 1h: commodity avg `-0.3465` n `12`; crypto_alt avg `-0.5473` n `234`; crypto_major avg `-0.472` n `8`; equity avg `-0.2918` n `141`; fx avg `0.0374` n `6`; index avg `-0.0954` n `26`; metal avg `-0.1314` n `20`; unknown avg `2.1615` n `926`
- 4h: commodity avg `-0.3174` n `12`; crypto_alt avg `-0.6116` n `234`; crypto_major avg `-0.612` n `8`; equity avg `-0.2611` n `141`; fx avg `-0.0108` n `6`; index avg `-0.0905` n `26`; metal avg `-0.13` n `20`; unknown avg `1.7037` n `860`
- 24h: commodity avg `-0.4749` n `12`; crypto_alt avg `0.4578` n `234`; crypto_major avg `-0.0454` n `8`; equity avg `0.1017` n `141`; fx avg `-0.0173` n `6`; index avg `-0.0476` n `26`; metal avg `-0.1464` n `20`; unknown avg `7.4266` n `827`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
