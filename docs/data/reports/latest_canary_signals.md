# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T05:52:30.189366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.77` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `-0.185` n `228`; crypto_major avg `-0.0484` n `8`; equity avg `-0.0466` n `74`; fx avg `-0.0051` n `6`; index avg `0.1074` n `23`; metal avg `-0.2644` n `18`; unknown avg `1.2159` n `545`
- 1h: commodity avg `0.0911` n `12`; crypto_alt avg `0.1549` n `228`; crypto_major avg `0.0016` n `8`; equity avg `-0.1559` n `74`; fx avg `-0.0108` n `6`; index avg `0.0621` n `23`; metal avg `-0.3786` n `18`; unknown avg `0.9519` n `545`
- 4h: commodity avg `-0.0666` n `12`; crypto_alt avg `0.6684` n `228`; crypto_major avg `0.2162` n `8`; equity avg `0.0548` n `74`; fx avg `-0.0149` n `6`; index avg `0.0579` n `23`; metal avg `-0.2776` n `18`; unknown avg `0.7636` n `545`
- 24h: commodity avg `-0.8492` n `12`; crypto_alt avg `2.8907` n `228`; crypto_major avg `2.7228` n `8`; equity avg `1.7255` n `74`; fx avg `0.0148` n `6`; index avg `0.8731` n `23`; metal avg `1.67` n `18`; unknown avg `3.8623` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
