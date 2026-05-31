# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T06:22:17.467694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.063` n `12`; crypto_alt avg `0.1006` n `228`; crypto_major avg `0.0315` n `8`; equity avg `0.089` n `69`; fx avg `0.0` n `6`; index avg `-0.0111` n `23`; metal avg `-0.0143` n `18`; unknown avg `-0.0635` n `421`
- 1h: commodity avg `0.0696` n `12`; crypto_alt avg `-0.2585` n `228`; crypto_major avg `-0.2402` n `8`; equity avg `0.116` n `69`; fx avg `0.0155` n `6`; index avg `-0.0097` n `23`; metal avg `-0.0316` n `18`; unknown avg `-0.1067` n `401`
- 4h: commodity avg `0.1434` n `12`; crypto_alt avg `-0.1786` n `228`; crypto_major avg `0.0091` n `8`; equity avg `0.2252` n `69`; fx avg `-0.0026` n `6`; index avg `-0.0281` n `23`; metal avg `-0.0002` n `18`; unknown avg `-0.1586` n `401`
- 24h: commodity avg `0.1776` n `12`; crypto_alt avg `0.4551` n `228`; crypto_major avg `2.2215` n `8`; equity avg `1.0513` n `69`; fx avg `0.0406` n `6`; index avg `-0.0044` n `23`; metal avg `-0.041` n `18`; unknown avg `0.3727` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
