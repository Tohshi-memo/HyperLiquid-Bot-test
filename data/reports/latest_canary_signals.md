# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T21:07:24.144581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0999` n `12`; crypto_alt avg `0.1079` n `228`; crypto_major avg `0.0374` n `8`; equity avg `0.0495` n `69`; fx avg `-0.0113` n `6`; index avg `-0.0371` n `23`; metal avg `-0.018` n `18`; unknown avg `-0.0517` n `421`
- 1h: commodity avg `-0.0648` n `12`; crypto_alt avg `0.2875` n `228`; crypto_major avg `0.1763` n `8`; equity avg `0.0638` n `69`; fx avg `-0.0185` n `6`; index avg `0.2387` n `23`; metal avg `-0.026` n `18`; unknown avg `1.2595` n `421`
- 4h: commodity avg `-0.1462` n `12`; crypto_alt avg `1.1902` n `228`; crypto_major avg `0.4979` n `8`; equity avg `0.1782` n `69`; fx avg `-0.0234` n `6`; index avg `0.3116` n `23`; metal avg `-0.0743` n `18`; unknown avg `0.6488` n `421`
- 24h: commodity avg `0.3619` n `12`; crypto_alt avg `-0.7621` n `228`; crypto_major avg `-0.3842` n `8`; equity avg `0.7628` n `69`; fx avg `-0.04` n `6`; index avg `0.3956` n `23`; metal avg `-0.183` n `18`; unknown avg `1.6705` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2827`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1968`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
