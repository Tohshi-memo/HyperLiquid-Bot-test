# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T10:37:33.154701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.0309` n `228`; crypto_major avg `-0.1478` n `8`; equity avg `0.0689` n `88`; fx avg `0.0088` n `6`; index avg `0.0079` n `23`; metal avg `0.0885` n `20`; unknown avg `0.0242` n `765`
- 1h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.0967` n `228`; crypto_major avg `-0.4264` n `8`; equity avg `0.1651` n `88`; fx avg `0.0281` n `6`; index avg `0.0329` n `23`; metal avg `0.0259` n `20`; unknown avg `-0.0247` n `765`
- 4h: commodity avg `-0.1575` n `12`; crypto_alt avg `0.3444` n `228`; crypto_major avg `-0.1223` n `8`; equity avg `0.1842` n `88`; fx avg `0.0236` n `6`; index avg `0.031` n `23`; metal avg `0.2544` n `20`; unknown avg `0.1469` n `763`
- 24h: commodity avg `-0.4607` n `12`; crypto_alt avg `-0.134` n `228`; crypto_major avg `-0.6` n `8`; equity avg `0.7145` n `88`; fx avg `0.123` n `6`; index avg `0.0406` n `23`; metal avg `-0.7043` n `20`; unknown avg `0.0045` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
