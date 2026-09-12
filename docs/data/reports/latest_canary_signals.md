# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T00:22:37.842360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.1349` n `233`; crypto_major avg `0.0766` n `8`; equity avg `0.008` n `136`; fx avg `0.0029` n `6`; index avg `0.0041` n `26`; metal avg `0.0073` n `20`; unknown avg `-0.1578` n `836`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `0.4821` n `233`; crypto_major avg `0.0961` n `8`; equity avg `0.0732` n `136`; fx avg `-0.0153` n `6`; index avg `0.0189` n `26`; metal avg `0.0041` n `20`; unknown avg `-0.2286` n `832`
- 4h: commodity avg `-0.1158` n `12`; crypto_alt avg `-0.2035` n `233`; crypto_major avg `-0.5435` n `8`; equity avg `0.0637` n `136`; fx avg `-0.0249` n `6`; index avg `0.0248` n `26`; metal avg `-0.0216` n `20`; unknown avg `4.2001` n `800`
- 24h: commodity avg `-0.6307` n `12`; crypto_alt avg `0.8695` n `233`; crypto_major avg `1.4062` n `8`; equity avg `0.9739` n `136`; fx avg `-0.1863` n `6`; index avg `0.3385` n `26`; metal avg `0.2545` n `20`; unknown avg `1.5754` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
