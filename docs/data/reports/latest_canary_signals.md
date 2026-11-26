# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T20:18:33.379157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `-0.0445` n `239`; crypto_major avg `-0.075` n `8`; equity avg `0.0337` n `168`; fx avg `0.0001` n `6`; index avg `0.0002` n `27`; metal avg `0.0093` n `20`; unknown avg `0.9405` n `1259`
- 1h: commodity avg `-0.0039` n `13`; crypto_alt avg `-0.0891` n `239`; crypto_major avg `0.0143` n `8`; equity avg `0.0762` n `168`; fx avg `0.0018` n `6`; index avg `0.0` n `27`; metal avg `0.0443` n `20`; unknown avg `-0.1061` n `1247`
- 4h: commodity avg `-0.0546` n `13`; crypto_alt avg `0.6747` n `239`; crypto_major avg `0.9304` n `8`; equity avg `0.2829` n `168`; fx avg `-0.0153` n `6`; index avg `0.0205` n `27`; metal avg `-0.0247` n `20`; unknown avg `8.295` n `1209`
- 24h: commodity avg `0.1339` n `13`; crypto_alt avg `1.6726` n `239`; crypto_major avg `1.0029` n `8`; equity avg `1.3869` n `168`; fx avg `-0.0399` n `6`; index avg `0.1013` n `27`; metal avg `0.1272` n `20`; unknown avg `12.9029` n `1031`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
