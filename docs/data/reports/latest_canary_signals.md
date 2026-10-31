# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T12:37:29.125483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `13`; crypto_alt avg `0.2236` n `238`; crypto_major avg `0.1639` n `8`; equity avg `0.0135` n `156`; fx avg `-0.0003` n `6`; index avg `-0.0004` n `27`; metal avg `0.0082` n `20`; unknown avg `0.0999` n `1262`
- 1h: commodity avg `0.0059` n `13`; crypto_alt avg `0.354` n `238`; crypto_major avg `0.245` n `8`; equity avg `0.0205` n `156`; fx avg `0.0144` n `6`; index avg `0.0009` n `27`; metal avg `0.0053` n `20`; unknown avg `0.8765` n `1250`
- 4h: commodity avg `0.0217` n `13`; crypto_alt avg `0.7382` n `238`; crypto_major avg `0.8497` n `8`; equity avg `0.0495` n `156`; fx avg `-0.0023` n `6`; index avg `-0.0108` n `27`; metal avg `0.0464` n `20`; unknown avg `16.7037` n `1218`
- 24h: commodity avg `-0.1249` n `13`; crypto_alt avg `0.7031` n `238`; crypto_major avg `-0.371` n `8`; equity avg `-1.0376` n `156`; fx avg `-0.0384` n `6`; index avg `-0.1072` n `27`; metal avg `-0.227` n `20`; unknown avg `3.6995` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
