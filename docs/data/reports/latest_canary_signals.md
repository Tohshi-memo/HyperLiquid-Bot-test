# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T12:52:28.075582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `12`; crypto_alt avg `-0.0251` n `230`; crypto_major avg `0.026` n `8`; equity avg `-0.0124` n `94`; fx avg `0.0295` n `6`; index avg `0.0054` n `25`; metal avg `-0.0978` n `20`; unknown avg `0.0211` n `768`
- 1h: commodity avg `0.205` n `12`; crypto_alt avg `-0.0533` n `230`; crypto_major avg `-0.3389` n `8`; equity avg `-0.1672` n `94`; fx avg `0.036` n `6`; index avg `-0.0559` n `25`; metal avg `-0.2461` n `20`; unknown avg `0.2137` n `768`
- 4h: commodity avg `0.3333` n `12`; crypto_alt avg `0.0551` n `230`; crypto_major avg `-0.3122` n `8`; equity avg `-0.7508` n `94`; fx avg `0.0004` n `6`; index avg `-0.2036` n `25`; metal avg `-0.3643` n `20`; unknown avg `0.0887` n `762`
- 24h: commodity avg `0.2761` n `12`; crypto_alt avg `-1.5842` n `230`; crypto_major avg `-1.9729` n `8`; equity avg `-3.6372` n `93`; fx avg `0.051` n `6`; index avg `-0.67` n `25`; metal avg `-0.5103` n `20`; unknown avg `0.0042` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
