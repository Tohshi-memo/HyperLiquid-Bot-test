# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T00:07:25.621353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0124` n `13`; crypto_alt avg `0.1894` n `238`; crypto_major avg `0.1203` n `8`; equity avg `0.3409` n `155`; fx avg `-0.0093` n `6`; index avg `0.072` n `27`; metal avg `-0.0196` n `20`; unknown avg `0.4251` n `1222`
- 1h: commodity avg `0.007` n `13`; crypto_alt avg `0.0913` n `238`; crypto_major avg `0.0487` n `8`; equity avg `0.0454` n `155`; fx avg `-0.023` n `6`; index avg `0.0113` n `27`; metal avg `-0.0303` n `20`; unknown avg `184.2334` n `1212`
- 4h: commodity avg `0.0521` n `13`; crypto_alt avg `-0.8115` n `238`; crypto_major avg `-0.496` n `8`; equity avg `-1.1077` n `155`; fx avg `-0.0432` n `6`; index avg `-0.1753` n `27`; metal avg `-0.1565` n `20`; unknown avg `3.0961` n `1076`
- 24h: commodity avg `0.0539` n `13`; crypto_alt avg `0.6554` n `238`; crypto_major avg `0.6451` n `8`; equity avg `0.9785` n `154`; fx avg `0.2068` n `6`; index avg `0.2079` n `27`; metal avg `-0.1845` n `20`; unknown avg `26.3681` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
