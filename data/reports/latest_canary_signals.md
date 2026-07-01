# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T12:22:32.327929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `0.0395` n `228`; crypto_major avg `0.0963` n `8`; equity avg `0.0855` n `88`; fx avg `-0.0036` n `6`; index avg `0.0332` n `23`; metal avg `0.0507` n `20`; unknown avg `0.4322` n `765`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.2413` n `228`; crypto_major avg `-0.2946` n `8`; equity avg `-0.1977` n `88`; fx avg `-0.0286` n `6`; index avg `-0.0239` n `23`; metal avg `-0.0604` n `20`; unknown avg `0.0112` n `765`
- 4h: commodity avg `-0.0474` n `12`; crypto_alt avg `0.3609` n `228`; crypto_major avg `-0.3254` n `8`; equity avg `0.1247` n `88`; fx avg `0.0151` n `6`; index avg `0.0565` n `23`; metal avg `0.3848` n `20`; unknown avg `0.2418` n `765`
- 24h: commodity avg `-0.6377` n `12`; crypto_alt avg `0.9935` n `228`; crypto_major avg `-0.1655` n `8`; equity avg `0.7938` n `88`; fx avg `0.1148` n `6`; index avg `0.01` n `23`; metal avg `-0.3015` n `20`; unknown avg `0.0994` n `743`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
