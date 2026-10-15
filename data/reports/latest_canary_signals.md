# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T18:52:31.737667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0655` n `13`; crypto_alt avg `0.0632` n `236`; crypto_major avg `0.1137` n `8`; equity avg `0.1063` n `151`; fx avg `-0.0068` n `6`; index avg `0.0085` n `26`; metal avg `0.005` n `20`; unknown avg `-0.4277` n `1136`
- 1h: commodity avg `-0.0857` n `13`; crypto_alt avg `0.0374` n `236`; crypto_major avg `-0.0591` n `8`; equity avg `-0.0786` n `151`; fx avg `-0.0051` n `6`; index avg `-0.0514` n `26`; metal avg `0.0089` n `20`; unknown avg `0.784` n `1134`
- 4h: commodity avg `0.0395` n `13`; crypto_alt avg `2.239` n `236`; crypto_major avg `1.3362` n `8`; equity avg `1.075` n `151`; fx avg `0.0139` n `6`; index avg `0.0995` n `26`; metal avg `-0.0332` n `20`; unknown avg `-0.3048` n `1124`
- 24h: commodity avg `-0.0627` n `13`; crypto_alt avg `0.8735` n `236`; crypto_major avg `0.6967` n `8`; equity avg `-0.937` n `151`; fx avg `0.2145` n `6`; index avg `-0.1931` n `26`; metal avg `0.4504` n `20`; unknown avg `0.1117` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0896`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0831`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0817`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0777`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0589`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0524`, n `666`, weak_sample_signal
