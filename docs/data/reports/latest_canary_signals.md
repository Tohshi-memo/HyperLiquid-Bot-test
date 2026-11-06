# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T11:37:22.839566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `13`; crypto_alt avg `0.2093` n `239`; crypto_major avg `0.1408` n `8`; equity avg `0.4016` n `158`; fx avg `0.0051` n `6`; index avg `0.0252` n `27`; metal avg `0.0706` n `20`; unknown avg `0.1715` n `1257`
- 1h: commodity avg `0.1003` n `13`; crypto_alt avg `0.3369` n `239`; crypto_major avg `0.0777` n `8`; equity avg `0.4162` n `158`; fx avg `0.0586` n `6`; index avg `-0.0003` n `27`; metal avg `0.0815` n `20`; unknown avg `1.0328` n `1241`
- 4h: commodity avg `-0.1146` n `13`; crypto_alt avg `1.5651` n `239`; crypto_major avg `1.1819` n `8`; equity avg `2.4572` n `158`; fx avg `0.0757` n `6`; index avg `0.3158` n `27`; metal avg `0.3163` n `20`; unknown avg `21.2505` n `1182`
- 24h: commodity avg `0.7934` n `13`; crypto_alt avg `-2.9605` n `239`; crypto_major avg `-5.1533` n `8`; equity avg `-4.4005` n `158`; fx avg `0.0264` n `6`; index avg `-0.6292` n `27`; metal avg `-0.3802` n `20`; unknown avg `15.8846` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
