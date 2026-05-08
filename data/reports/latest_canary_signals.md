# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T12:07:17.454418+00:00`
- Correlation status: `ready`
- Asset price records: `644`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1163` n `12`; crypto_alt avg `-0.0508` n `228`; crypto_major avg `-0.0197` n `8`; equity avg `-0.0737` n `65`; fx avg `-0.0128` n `5`; index avg `0.0313` n `23`; metal avg `0.0284` n `18`; unknown avg `0.2245` n `375`
- 1h: commodity avg `-0.0975` n `12`; crypto_alt avg `0.1752` n `228`; crypto_major avg `0.0779` n `8`; equity avg `0.0228` n `65`; fx avg `-0.0012` n `5`; index avg `0.0781` n `23`; metal avg `-0.1541` n `18`; unknown avg `0.265` n `375`
- 4h: commodity avg `-0.2054` n `12`; crypto_alt avg `0.4479` n `228`; crypto_major avg `0.3297` n `8`; equity avg `0.1506` n `65`; fx avg `0.0114` n `5`; index avg `0.149` n `23`; metal avg `0.2347` n `18`; unknown avg `0.444` n `375`
- 24h: commodity avg `1.4171` n `12`; crypto_alt avg `0.9372` n `228`; crypto_major avg `-1.2984` n `8`; equity avg `-0.5248` n `65`; fx avg `0.2497` n `5`; index avg `-0.3605` n `23`; metal avg `-0.704` n `18`; unknown avg `-0.0591` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1341`, n `636`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1339`, n `636`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.109`, n `640`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `640`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0916`, n `640`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `640`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `636`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0832`, n `636`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `636`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `640`, weak_sample_signal
