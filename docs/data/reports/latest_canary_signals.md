# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T02:07:28.582254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `13`; crypto_alt avg `-0.0894` n `239`; crypto_major avg `-0.118` n `8`; equity avg `0.0156` n `166`; fx avg `0.0194` n `6`; index avg `-0.0087` n `27`; metal avg `-0.1385` n `20`; unknown avg `159.6324` n `1253`
- 1h: commodity avg `0.009` n `13`; crypto_alt avg `-0.1779` n `239`; crypto_major avg `-0.322` n `8`; equity avg `0.2061` n `166`; fx avg `0.0583` n `6`; index avg `0.0006` n `27`; metal avg `-0.1286` n `20`; unknown avg `317.9366` n `1257`
- 4h: commodity avg `-0.2739` n `13`; crypto_alt avg `-0.4192` n `239`; crypto_major avg `-0.4308` n `8`; equity avg `0.4992` n `166`; fx avg `0.108` n `6`; index avg `0.0511` n `27`; metal avg `0.1188` n `20`; unknown avg `0.2025` n `1214`
- 24h: commodity avg `-0.4375` n `13`; crypto_alt avg `0.2401` n `239`; crypto_major avg `0.3442` n `8`; equity avg `1.2518` n `166`; fx avg `0.2037` n `6`; index avg `0.1218` n `27`; metal avg `0.1175` n `20`; unknown avg `195.9385` n `1025`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
