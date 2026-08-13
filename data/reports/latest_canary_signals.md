# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T15:07:30.595607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0548` n `12`; crypto_alt avg `-0.0815` n `230`; crypto_major avg `-0.0432` n `8`; equity avg `-0.0175` n `113`; fx avg `0.0133` n `6`; index avg `0.0067` n `25`; metal avg `-0.0555` n `20`; unknown avg `0.1141` n `787`
- 1h: commodity avg `0.2194` n `12`; crypto_alt avg `0.2084` n `230`; crypto_major avg `0.1965` n `8`; equity avg `0.2914` n `113`; fx avg `0.0082` n `6`; index avg `0.0735` n `25`; metal avg `-0.0127` n `20`; unknown avg `-0.0568` n `787`
- 4h: commodity avg `-0.0875` n `12`; crypto_alt avg `0.3899` n `230`; crypto_major avg `0.3894` n `8`; equity avg `1.666` n `113`; fx avg `-0.0186` n `6`; index avg `0.2923` n `25`; metal avg `-0.1391` n `20`; unknown avg `0.1526` n `787`
- 24h: commodity avg `-0.475` n `12`; crypto_alt avg `0.1006` n `230`; crypto_major avg `0.5718` n `8`; equity avg `1.9349` n `113`; fx avg `0.0205` n `6`; index avg `0.3387` n `25`; metal avg `-0.533` n `20`; unknown avg `0.3282` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1947`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
