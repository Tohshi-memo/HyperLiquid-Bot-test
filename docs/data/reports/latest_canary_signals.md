# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T19:52:41.268563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0647` n `12`; crypto_alt avg `-0.0763` n `234`; crypto_major avg `0.0075` n `8`; equity avg `-0.2559` n `141`; fx avg `0.0098` n `6`; index avg `-0.0356` n `26`; metal avg `0.0052` n `20`; unknown avg `538.5347` n `943`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `-0.2732` n `234`; crypto_major avg `0.0417` n `8`; equity avg `-0.3168` n `141`; fx avg `0.0014` n `6`; index avg `-0.0357` n `26`; metal avg `-0.0247` n `20`; unknown avg `39.7637` n `941`
- 4h: commodity avg `0.0462` n `12`; crypto_alt avg `-0.1521` n `234`; crypto_major avg `0.2932` n `8`; equity avg `-0.3174` n `141`; fx avg `-0.0198` n `6`; index avg `-0.0567` n `26`; metal avg `0.0472` n `20`; unknown avg `12.5167` n `921`
- 24h: commodity avg `0.6654` n `12`; crypto_alt avg `-3.2119` n `234`; crypto_major avg `-3.2299` n `8`; equity avg `-1.7763` n `140`; fx avg `0.0006` n `6`; index avg `-0.4316` n `26`; metal avg `-0.9342` n `20`; unknown avg `19.2884` n `878`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
