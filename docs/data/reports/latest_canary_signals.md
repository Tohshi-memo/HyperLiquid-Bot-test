# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T06:52:20.523685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `12`; crypto_alt avg `-0.2667` n `228`; crypto_major avg `-0.081` n `8`; equity avg `-0.0311` n `69`; fx avg `0.0` n `6`; index avg `0.0171` n `23`; metal avg `0.0046` n `18`; unknown avg `0.03` n `421`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.1995` n `228`; crypto_major avg `-0.0416` n `8`; equity avg `-0.0021` n `69`; fx avg `-0.0016` n `6`; index avg `0.0606` n `23`; metal avg `0.0207` n `18`; unknown avg `0.1143` n `401`
- 4h: commodity avg `-0.082` n `12`; crypto_alt avg `-0.5204` n `228`; crypto_major avg `-0.0251` n `8`; equity avg `0.1368` n `69`; fx avg `0.0024` n `6`; index avg `0.1323` n `23`; metal avg `-0.0635` n `18`; unknown avg `0.2352` n `401`
- 24h: commodity avg `-0.2453` n `12`; crypto_alt avg `1.2987` n `228`; crypto_major avg `1.7571` n `8`; equity avg `0.7337` n `69`; fx avg `0.0369` n `6`; index avg `0.0743` n `23`; metal avg `-0.1072` n `18`; unknown avg `0.8117` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
