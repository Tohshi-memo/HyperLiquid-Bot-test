# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T07:37:34.189496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0438` n `12`; crypto_alt avg `0.0198` n `230`; crypto_major avg `-0.0508` n `8`; equity avg `-0.0888` n `108`; fx avg `0.0326` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0279` n `20`; unknown avg `0.0117` n `782`
- 1h: commodity avg `-0.0475` n `12`; crypto_alt avg `0.0892` n `230`; crypto_major avg `0.0073` n `8`; equity avg `0.0228` n `108`; fx avg `0.0499` n `6`; index avg `0.0198` n `25`; metal avg `0.0307` n `20`; unknown avg `0.0745` n `782`
- 4h: commodity avg `0.134` n `12`; crypto_alt avg `0.5247` n `230`; crypto_major avg `0.3527` n `8`; equity avg `-0.1255` n `108`; fx avg `0.1103` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0484` n `20`; unknown avg `0.0906` n `750`
- 24h: commodity avg `-0.1766` n `12`; crypto_alt avg `0.3777` n `230`; crypto_major avg `0.1782` n `8`; equity avg `-1.8184` n `108`; fx avg `0.0579` n `6`; index avg `-0.3357` n `25`; metal avg `0.1763` n `20`; unknown avg `0.9162` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1945`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
