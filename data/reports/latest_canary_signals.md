# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T02:22:35.489929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `13`; crypto_alt avg `-0.0195` n `239`; crypto_major avg `-0.0228` n `8`; equity avg `0.0204` n `158`; fx avg `-0.0005` n `6`; index avg `-0.0121` n `27`; metal avg `-0.0007` n `20`; unknown avg `0.3085` n `1262`
- 1h: commodity avg `0.0304` n `13`; crypto_alt avg `-0.2002` n `239`; crypto_major avg `-0.1381` n `8`; equity avg `-0.0316` n `158`; fx avg `0.0191` n `6`; index avg `-0.0206` n `27`; metal avg `-0.0147` n `20`; unknown avg `-0.0185` n `1254`
- 4h: commodity avg `-0.025` n `13`; crypto_alt avg `-0.3822` n `239`; crypto_major avg `-0.1169` n `8`; equity avg `0.0342` n `158`; fx avg `0.0236` n `6`; index avg `-0.0097` n `27`; metal avg `-0.0128` n `20`; unknown avg `-0.2374` n `1232`
- 24h: commodity avg `0.1006` n `13`; crypto_alt avg `-1.9478` n `239`; crypto_major avg `-1.086` n `8`; equity avg `-0.1603` n `158`; fx avg `0.0084` n `6`; index avg `0.0276` n `27`; metal avg `-0.0434` n `20`; unknown avg `160.8654` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
