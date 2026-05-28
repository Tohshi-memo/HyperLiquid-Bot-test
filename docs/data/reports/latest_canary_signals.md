# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T02:37:17.713995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0435` n `12`; crypto_alt avg `-0.0396` n `228`; crypto_major avg `0.0195` n `8`; equity avg `-0.0224` n `67`; fx avg `-0.0028` n `6`; index avg `-0.0122` n `23`; metal avg `0.1658` n `18`; unknown avg `0.1444` n `419`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `0.1326` n `228`; crypto_major avg `-0.197` n `8`; equity avg `-0.2915` n `67`; fx avg `-0.0339` n `6`; index avg `-0.0974` n `23`; metal avg `-0.2532` n `18`; unknown avg `-0.521` n `419`
- 4h: commodity avg `0.1695` n `12`; crypto_alt avg `-0.7508` n `228`; crypto_major avg `-0.8665` n `8`; equity avg `-0.5428` n `67`; fx avg `-0.0006` n `6`; index avg `-0.2253` n `23`; metal avg `-1.0321` n `18`; unknown avg `-0.3107` n `419`
- 24h: commodity avg `-0.674` n `12`; crypto_alt avg `-2.1333` n `228`; crypto_major avg `-1.842` n `8`; equity avg `-0.9993` n `67`; fx avg `-0.0546` n `6`; index avg `-0.9446` n `23`; metal avg `-2.0132` n `18`; unknown avg `-1.0755` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
