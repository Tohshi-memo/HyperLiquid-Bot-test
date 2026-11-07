# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T13:07:28.015447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0305` n `13`; crypto_alt avg `0.108` n `239`; crypto_major avg `-0.0395` n `8`; equity avg `0.0673` n `158`; fx avg `0.0048` n `6`; index avg `0.0077` n `27`; metal avg `0.0048` n `20`; unknown avg `-0.0203` n `1257`
- 1h: commodity avg `-0.0543` n `13`; crypto_alt avg `0.0011` n `239`; crypto_major avg `-0.2648` n `8`; equity avg `0.1513` n `158`; fx avg `0.0563` n `6`; index avg `0.0142` n `27`; metal avg `0.0037` n `20`; unknown avg `-0.0075` n `1255`
- 4h: commodity avg `0.0039` n `13`; crypto_alt avg `-0.5176` n `239`; crypto_major avg `-0.6146` n `8`; equity avg `-0.164` n `158`; fx avg `0.0553` n `6`; index avg `-0.0261` n `27`; metal avg `-0.001` n `20`; unknown avg `129.1449` n `1249`
- 24h: commodity avg `-0.0798` n `13`; crypto_alt avg `-1.2912` n `239`; crypto_major avg `-0.5879` n `8`; equity avg `-0.2276` n `158`; fx avg `0.0145` n `6`; index avg `0.0102` n `27`; metal avg `0.0322` n `20`; unknown avg `-0.3553` n `1117`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
