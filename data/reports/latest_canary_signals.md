# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T01:52:30.677976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `13`; crypto_alt avg `-0.1824` n `235`; crypto_major avg `-0.1356` n `8`; equity avg `0.0044` n `144`; fx avg `-0.0105` n `6`; index avg `-0.0142` n `26`; metal avg `-0.0373` n `20`; unknown avg `0.2821` n `1079`
- 1h: commodity avg `0.0464` n `13`; crypto_alt avg `-0.4902` n `235`; crypto_major avg `-0.3556` n `8`; equity avg `-0.1565` n `144`; fx avg `0.0167` n `6`; index avg `-0.0361` n `26`; metal avg `-0.1189` n `20`; unknown avg `0.136` n `1077`
- 4h: commodity avg `0.0718` n `13`; crypto_alt avg `-1.0619` n `235`; crypto_major avg `-0.3713` n `8`; equity avg `-0.09` n `144`; fx avg `0.0444` n `6`; index avg `-0.0524` n `26`; metal avg `-0.0592` n `20`; unknown avg `0.3353` n `1069`
- 24h: commodity avg `-0.0543` n `13`; crypto_alt avg `-0.7143` n `235`; crypto_major avg `-0.3263` n `8`; equity avg `-0.2218` n `144`; fx avg `0.0089` n `6`; index avg `0.0226` n `26`; metal avg `-0.1225` n `20`; unknown avg `626.9044` n `798`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
