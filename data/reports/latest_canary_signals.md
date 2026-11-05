# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T08:22:27.213551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0448` n `13`; crypto_alt avg `0.4607` n `239`; crypto_major avg `0.2856` n `8`; equity avg `0.2111` n `158`; fx avg `0.0161` n `6`; index avg `0.0379` n `27`; metal avg `0.029` n `20`; unknown avg `0.5351` n `1265`
- 1h: commodity avg `0.0548` n `13`; crypto_alt avg `0.2517` n `239`; crypto_major avg `0.2368` n `8`; equity avg `0.1` n `158`; fx avg `-0.0178` n `6`; index avg `0.0563` n `27`; metal avg `0.031` n `20`; unknown avg `1.0654` n `1241`
- 4h: commodity avg `0.3292` n `13`; crypto_alt avg `-0.0434` n `239`; crypto_major avg `0.3543` n `8`; equity avg `0.1984` n `158`; fx avg `-0.0555` n `6`; index avg `0.0477` n `27`; metal avg `-0.0961` n `20`; unknown avg `1.0185` n `1207`
- 24h: commodity avg `-1.6895` n `13`; crypto_alt avg `0.4932` n `239`; crypto_major avg `1.8343` n `8`; equity avg `-2.6342` n `158`; fx avg `0.0182` n `6`; index avg `-0.1343` n `27`; metal avg `0.7172` n `20`; unknown avg `31.6797` n `1006`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2498`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
