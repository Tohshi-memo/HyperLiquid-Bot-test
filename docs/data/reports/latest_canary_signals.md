# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T23:37:32.880563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.2581` n `234`; crypto_major avg `-0.0459` n `8`; equity avg `-0.0254` n `141`; fx avg `-0.006` n `6`; index avg `-0.0017` n `26`; metal avg `-0.049` n `20`; unknown avg `-0.0417` n `945`
- 1h: commodity avg `-0.049` n `12`; crypto_alt avg `0.0833` n `234`; crypto_major avg `0.0342` n `8`; equity avg `-0.0273` n `141`; fx avg `-0.0012` n `6`; index avg `-0.0147` n `26`; metal avg `-0.0569` n `20`; unknown avg `-0.2908` n `943`
- 4h: commodity avg `-0.1193` n `12`; crypto_alt avg `-0.2747` n `234`; crypto_major avg `0.0802` n `8`; equity avg `-0.1157` n `141`; fx avg `-0.0135` n `6`; index avg `-0.0069` n `26`; metal avg `0.0154` n `20`; unknown avg `-0.7482` n `845`
- 24h: commodity avg `0.5032` n `12`; crypto_alt avg `-4.6275` n `234`; crypto_major avg `-3.2153` n `8`; equity avg `-1.7082` n `140`; fx avg `0.0222` n `6`; index avg `-0.3777` n `26`; metal avg `-0.8916` n `20`; unknown avg `584.4496` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
