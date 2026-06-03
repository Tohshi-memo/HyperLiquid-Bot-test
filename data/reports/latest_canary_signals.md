# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T18:37:34.810347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0894` n `12`; crypto_alt avg `0.1384` n `228`; crypto_major avg `0.1394` n `8`; equity avg `0.0281` n `73`; fx avg `0.0062` n `6`; index avg `0.041` n `23`; metal avg `-0.0687` n `18`; unknown avg `0.8876` n `419`
- 1h: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.6548` n `228`; crypto_major avg `-0.4825` n `8`; equity avg `0.1607` n `73`; fx avg `0.0155` n `6`; index avg `0.1118` n `23`; metal avg `-0.1778` n `18`; unknown avg `-0.2582` n `419`
- 4h: commodity avg `0.3763` n `12`; crypto_alt avg `-1.1773` n `228`; crypto_major avg `-0.9758` n `8`; equity avg `-0.594` n `73`; fx avg `0.0119` n `6`; index avg `-0.1822` n `23`; metal avg `-0.6761` n `18`; unknown avg `-0.2887` n `419`
- 24h: commodity avg `0.7909` n `12`; crypto_alt avg `0.6001` n `228`; crypto_major avg `-2.1568` n `8`; equity avg `-1.6095` n `72`; fx avg `0.0441` n `6`; index avg `-0.1142` n `23`; metal avg `-2.0303` n `18`; unknown avg `-0.0905` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
