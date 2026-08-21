# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T11:22:23.042292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0429` n `12`; crypto_alt avg `-0.0194` n `230`; crypto_major avg `-0.3626` n `8`; equity avg `0.1167` n `121`; fx avg `-0.0077` n `6`; index avg `0.0127` n `25`; metal avg `0.0772` n `20`; unknown avg `0.1075` n `793`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `0.451` n `230`; crypto_major avg `-0.2299` n `8`; equity avg `-0.0118` n `121`; fx avg `-0.0026` n `6`; index avg `0.0192` n `25`; metal avg `0.1538` n `20`; unknown avg `0.1347` n `793`
- 4h: commodity avg `0.1787` n `12`; crypto_alt avg `2.4264` n `230`; crypto_major avg `1.3715` n `8`; equity avg `0.2315` n `121`; fx avg `-0.0104` n `6`; index avg `-0.006` n `25`; metal avg `0.2191` n `20`; unknown avg `0.4847` n `793`
- 24h: commodity avg `0.1227` n `12`; crypto_alt avg `7.4191` n `230`; crypto_major avg `6.775` n `8`; equity avg `0.9046` n `121`; fx avg `-0.0959` n `6`; index avg `0.0725` n `25`; metal avg `0.9444` n `20`; unknown avg `2.5393` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2277`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1934`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
