# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T12:37:32.396965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.35` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `0.0829` n `233`; crypto_major avg `0.0596` n `8`; equity avg `0.0092` n `136`; fx avg `-0.0036` n `6`; index avg `0.0007` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.6821` n `832`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `0.2172` n `233`; crypto_major avg `0.0528` n `8`; equity avg `0.0057` n `136`; fx avg `0.0008` n `6`; index avg `0.0` n `26`; metal avg `0.0251` n `20`; unknown avg `0.8268` n `830`
- 4h: commodity avg `0.0521` n `12`; crypto_alt avg `0.2641` n `233`; crypto_major avg `0.3923` n `8`; equity avg `0.0673` n `136`; fx avg `-0.0101` n `6`; index avg `-0.001` n `26`; metal avg `0.0309` n `20`; unknown avg `0.0303` n `830`
- 24h: commodity avg `0.006` n `12`; crypto_alt avg `1.1718` n `233`; crypto_major avg `0.6527` n `8`; equity avg `-0.1154` n `136`; fx avg `-0.0482` n `6`; index avg `0.0776` n `26`; metal avg `0.0318` n `20`; unknown avg `0.9457` n `692`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
