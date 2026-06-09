# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T23:52:22.548377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `12`; crypto_alt avg `0.1293` n `228`; crypto_major avg `0.2761` n `8`; equity avg `0.1078` n `74`; fx avg `0.0167` n `6`; index avg `0.0153` n `23`; metal avg `-0.0793` n `18`; unknown avg `0.0811` n `547`
- 1h: commodity avg `-0.0638` n `12`; crypto_alt avg `0.1294` n `228`; crypto_major avg `0.0294` n `8`; equity avg `0.1718` n `74`; fx avg `0.0015` n `6`; index avg `0.0206` n `23`; metal avg `-0.2586` n `18`; unknown avg `-0.1448` n `547`
- 4h: commodity avg `0.2042` n `12`; crypto_alt avg `-0.2819` n `228`; crypto_major avg `-0.5438` n `8`; equity avg `-0.1745` n `74`; fx avg `-0.0162` n `6`; index avg `0.341` n `23`; metal avg `-0.6184` n `18`; unknown avg `-0.063` n `547`
- 24h: commodity avg `-0.5926` n `12`; crypto_alt avg `-1.0679` n `228`; crypto_major avg `-2.8081` n `8`; equity avg `-2.2723` n `74`; fx avg `0.0602` n `6`; index avg `-0.9286` n `23`; metal avg `-1.8765` n `18`; unknown avg `-0.4294` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0373`, n `668`, weak_sample_signal
