# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T01:37:27.160798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.4322` n `234`; crypto_major avg `-0.4297` n `8`; equity avg `-0.077` n `137`; fx avg `0.0145` n `6`; index avg `-0.0095` n `27`; metal avg `-0.0336` n `20`; unknown avg `0.1105` n `919`
- 1h: commodity avg `0.0524` n `12`; crypto_alt avg `-0.595` n `234`; crypto_major avg `-0.403` n `8`; equity avg `-0.1955` n `137`; fx avg `0.0384` n `6`; index avg `-0.0303` n `27`; metal avg `0.0339` n `20`; unknown avg `-0.2845` n `917`
- 4h: commodity avg `-0.0379` n `12`; crypto_alt avg `-0.4749` n `234`; crypto_major avg `-0.1187` n `8`; equity avg `-0.0534` n `137`; fx avg `0.1385` n `6`; index avg `0.0079` n `27`; metal avg `-0.0059` n `20`; unknown avg `-0.2117` n `863`
- 24h: commodity avg `0.3856` n `12`; crypto_alt avg `-4.2168` n `234`; crypto_major avg `-4.1659` n `8`; equity avg `-1.5264` n `137`; fx avg `0.3179` n `6`; index avg `-0.1407` n `27`; metal avg `0.1763` n `20`; unknown avg `0.6309` n `802`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
