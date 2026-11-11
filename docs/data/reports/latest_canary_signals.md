# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T09:22:29.730004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1835` n `13`; crypto_alt avg `-0.0179` n `239`; crypto_major avg `0.0027` n `8`; equity avg `-0.1136` n `161`; fx avg `0.0078` n `6`; index avg `-0.0497` n `27`; metal avg `-0.0337` n `20`; unknown avg `-0.0292` n `1245`
- 1h: commodity avg `0.177` n `13`; crypto_alt avg `-0.3876` n `239`; crypto_major avg `-0.3145` n `8`; equity avg `-0.0329` n `161`; fx avg `-0.0267` n `6`; index avg `-0.035` n `27`; metal avg `0.0037` n `20`; unknown avg `-0.264` n `1239`
- 4h: commodity avg `0.2125` n `13`; crypto_alt avg `-0.7787` n `239`; crypto_major avg `-0.2872` n `8`; equity avg `0.468` n `161`; fx avg `-0.0588` n `6`; index avg `-0.0338` n `27`; metal avg `0.042` n `20`; unknown avg `-0.2277` n `1197`
- 24h: commodity avg `0.7217` n `13`; crypto_alt avg `-1.383` n `239`; crypto_major avg `-1.949` n `8`; equity avg `1.8965` n `161`; fx avg `-0.2457` n `6`; index avg `0.1878` n `27`; metal avg `0.0902` n `20`; unknown avg `49.939` n `1175`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
