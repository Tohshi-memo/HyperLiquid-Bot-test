# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T15:22:23.988705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `-0.0731` n `228`; crypto_major avg `0.0309` n `8`; equity avg `-0.0421` n `69`; fx avg `-0.0006` n `6`; index avg `-0.0249` n `23`; metal avg `0.0068` n `18`; unknown avg `-0.0227` n `421`
- 1h: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.049` n `228`; crypto_major avg `0.3067` n `8`; equity avg `0.0158` n `69`; fx avg `0.0035` n `6`; index avg `-0.0159` n `23`; metal avg `-0.0188` n `18`; unknown avg `0.0013` n `421`
- 4h: commodity avg `0.182` n `12`; crypto_alt avg `0.3776` n `228`; crypto_major avg `0.8771` n `8`; equity avg `0.3598` n `69`; fx avg `0.0241` n `6`; index avg `0.1567` n `23`; metal avg `-0.0501` n `18`; unknown avg `0.2276` n `421`
- 24h: commodity avg `0.374` n `12`; crypto_alt avg `1.3363` n `228`; crypto_major avg `2.1017` n `8`; equity avg `1.3857` n `69`; fx avg `0.0165` n `6`; index avg `0.3531` n `23`; metal avg `-0.5643` n `18`; unknown avg `0.1573` n `400`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
