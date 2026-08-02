# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T22:37:28.714179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0306` n `12`; crypto_alt avg `-0.2404` n `230`; crypto_major avg `-0.2986` n `8`; equity avg `-0.0154` n `102`; fx avg `-0.045` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0093` n `20`; unknown avg `0.1312` n `783`
- 1h: commodity avg `-0.1804` n `12`; crypto_alt avg `-0.1299` n `230`; crypto_major avg `-0.0385` n `8`; equity avg `-0.0733` n `102`; fx avg `-0.0304` n `6`; index avg `-0.0462` n `25`; metal avg `-0.1534` n `20`; unknown avg `1.5619` n `783`
- 4h: commodity avg `-0.1131` n `12`; crypto_alt avg `-0.049` n `230`; crypto_major avg `0.1111` n `8`; equity avg `0.2081` n `102`; fx avg `0.099` n `6`; index avg `0.0242` n `25`; metal avg `-0.0718` n `20`; unknown avg `2.0056` n `782`
- 24h: commodity avg `-1.2776` n `12`; crypto_alt avg `1.1506` n `230`; crypto_major avg `1.7198` n `8`; equity avg `1.5555` n `102`; fx avg `-0.0488` n `6`; index avg `0.3279` n `25`; metal avg `0.1998` n `20`; unknown avg `1.619` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
