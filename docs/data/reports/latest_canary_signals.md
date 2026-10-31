# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T03:07:24.854453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `13`; crypto_alt avg `-0.0707` n `238`; crypto_major avg `-0.1505` n `8`; equity avg `0.016` n `156`; fx avg `0.011` n `6`; index avg `-0.004` n `27`; metal avg `-0.007` n `20`; unknown avg `-0.0232` n `1252`
- 1h: commodity avg `0.1116` n `13`; crypto_alt avg `0.0235` n `238`; crypto_major avg `-0.0053` n `8`; equity avg `0.0511` n `156`; fx avg `-0.0077` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0024` n `20`; unknown avg `-0.2469` n `1250`
- 4h: commodity avg `0.0295` n `13`; crypto_alt avg `-0.1014` n `238`; crypto_major avg `0.2497` n `8`; equity avg `0.147` n `156`; fx avg `0.0189` n `6`; index avg `0.0023` n `27`; metal avg `-0.009` n `20`; unknown avg `-0.0394` n `1241`
- 24h: commodity avg `-0.0753` n `13`; crypto_alt avg `3.7516` n `238`; crypto_major avg `0.4182` n `8`; equity avg `-2.0296` n `156`; fx avg `-0.099` n `6`; index avg `-0.0589` n `27`; metal avg `-0.6159` n `20`; unknown avg `-0.723` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
