# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T17:22:29.647196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.7436` n `230`; crypto_major avg `-0.7376` n `8`; equity avg `-0.1871` n `121`; fx avg `0.0028` n `6`; index avg `-0.0329` n `25`; metal avg `-0.0529` n `20`; unknown avg `0.0372` n `793`
- 1h: commodity avg `0.0862` n `12`; crypto_alt avg `-0.2821` n `230`; crypto_major avg `-0.154` n `8`; equity avg `-0.1895` n `121`; fx avg `0.0059` n `6`; index avg `-0.0181` n `25`; metal avg `0.0308` n `20`; unknown avg `0.0259` n `793`
- 4h: commodity avg `0.0357` n `12`; crypto_alt avg `0.5959` n `230`; crypto_major avg `0.475` n `8`; equity avg `-0.4731` n `121`; fx avg `0.0131` n `6`; index avg `-0.0352` n `25`; metal avg `0.0068` n `20`; unknown avg `0.1556` n `793`
- 24h: commodity avg `0.3356` n `12`; crypto_alt avg `6.3116` n `230`; crypto_major avg `3.3306` n `8`; equity avg `1.171` n `121`; fx avg `-0.0978` n `6`; index avg `0.0932` n `25`; metal avg `0.6514` n `20`; unknown avg `1.1143` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2369`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.191`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
