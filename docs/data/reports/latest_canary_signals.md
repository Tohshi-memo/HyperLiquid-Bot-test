# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T18:37:24.381637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `0.0697` n `230`; crypto_major avg `0.1834` n `8`; equity avg `0.0341` n `92`; fx avg `0.0` n `6`; index avg `-0.032` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0036` n `765`
- 1h: commodity avg `0.0416` n `12`; crypto_alt avg `-0.1592` n `230`; crypto_major avg `-0.0419` n `8`; equity avg `0.0007` n `92`; fx avg `-0.019` n `6`; index avg `-0.0223` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0031` n `765`
- 4h: commodity avg `0.1557` n `12`; crypto_alt avg `0.0914` n `230`; crypto_major avg `0.3518` n `8`; equity avg `0.0044` n `92`; fx avg `-0.0292` n `6`; index avg `0.0118` n `25`; metal avg `-0.0069` n `20`; unknown avg `-0.0751` n `759`
- 24h: commodity avg `0.5748` n `12`; crypto_alt avg `-1.5071` n `230`; crypto_major avg `-0.6287` n `8`; equity avg `-0.2179` n `92`; fx avg `-0.0055` n `6`; index avg `-0.1106` n `25`; metal avg `-0.1031` n `20`; unknown avg `0.1421` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
