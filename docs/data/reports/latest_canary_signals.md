# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T22:52:25.342874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0571` n `12`; crypto_alt avg `0.0471` n `230`; crypto_major avg `0.1113` n `8`; equity avg `0.0529` n `103`; fx avg `0.0017` n `6`; index avg `0.016` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.012` n `784`
- 1h: commodity avg `-0.0869` n `12`; crypto_alt avg `-0.2936` n `230`; crypto_major avg `-0.1909` n `8`; equity avg `0.1642` n `103`; fx avg `0.0164` n `6`; index avg `0.0379` n `25`; metal avg `-0.0357` n `20`; unknown avg `-0.0647` n `784`
- 4h: commodity avg `-0.1322` n `12`; crypto_alt avg `-0.2302` n `230`; crypto_major avg `-0.4471` n `8`; equity avg `0.5455` n `103`; fx avg `0.0551` n `6`; index avg `0.1155` n `25`; metal avg `0.0824` n `20`; unknown avg `0.0428` n `784`
- 24h: commodity avg `-0.1914` n `12`; crypto_alt avg `0.2474` n `230`; crypto_major avg `-0.0179` n `8`; equity avg `2.2163` n `103`; fx avg `-0.2478` n `6`; index avg `0.1549` n `25`; metal avg `-0.2847` n `20`; unknown avg `0.0172` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
