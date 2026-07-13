# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T08:52:27.982526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.119` n `12`; crypto_alt avg `0.2546` n `230`; crypto_major avg `0.2697` n `8`; equity avg `0.1149` n `92`; fx avg `-0.0247` n `6`; index avg `0.0206` n `25`; metal avg `0.0235` n `20`; unknown avg `-0.0379` n `766`
- 1h: commodity avg `-0.2044` n `12`; crypto_alt avg `0.2256` n `230`; crypto_major avg `0.3316` n `8`; equity avg `0.3872` n `92`; fx avg `-0.0227` n `6`; index avg `0.1011` n `25`; metal avg `0.1845` n `20`; unknown avg `-0.0112` n `766`
- 4h: commodity avg `-0.3366` n `12`; crypto_alt avg `0.7384` n `230`; crypto_major avg `0.5297` n `8`; equity avg `0.3809` n `92`; fx avg `-0.0699` n `6`; index avg `0.1406` n `25`; metal avg `0.339` n `20`; unknown avg `0.0533` n `750`
- 24h: commodity avg `-0.2892` n `12`; crypto_alt avg `-0.9742` n `230`; crypto_major avg `-0.7553` n `8`; equity avg `-2.0042` n `92`; fx avg `-0.0304` n `6`; index avg `-0.409` n `25`; metal avg `-0.1368` n `20`; unknown avg `0.0113` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
