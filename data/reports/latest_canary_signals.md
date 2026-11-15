# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T11:22:33.345832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7023` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `0.1302` n `239`; crypto_major avg `0.0378` n `8`; equity avg `0.0633` n `162`; fx avg `-0.0074` n `6`; index avg `0.0047` n `27`; metal avg `0.0007` n `20`; unknown avg `0.1611` n `1261`
- 1h: commodity avg `-0.0167` n `13`; crypto_alt avg `-0.0445` n `239`; crypto_major avg `0.0225` n `8`; equity avg `0.0469` n `162`; fx avg `-0.0156` n `6`; index avg `0.0044` n `27`; metal avg `-0.0055` n `20`; unknown avg `0.7357` n `1261`
- 4h: commodity avg `-0.0612` n `13`; crypto_alt avg `1.022` n `239`; crypto_major avg `1.7949` n `8`; equity avg `0.365` n `162`; fx avg `-0.0261` n `6`; index avg `0.0446` n `27`; metal avg `0.0926` n `20`; unknown avg `0.8425` n `1245`
- 24h: commodity avg `0.0173` n `13`; crypto_alt avg `-3.8556` n `239`; crypto_major avg `-3.1147` n `8`; equity avg `-0.6756` n `162`; fx avg `0.0291` n `6`; index avg `-0.0517` n `27`; metal avg `-0.3351` n `20`; unknown avg `-0.5336` n `1136`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
