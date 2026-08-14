# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T07:52:24.261407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `-0.0049` n `230`; crypto_major avg `-0.0294` n `8`; equity avg `0.0652` n `113`; fx avg `-0.0274` n `6`; index avg `0.0079` n `25`; metal avg `0.0647` n `20`; unknown avg `-0.0183` n `787`
- 1h: commodity avg `0.1051` n `12`; crypto_alt avg `-0.1643` n `230`; crypto_major avg `-0.0528` n `8`; equity avg `0.0543` n `113`; fx avg `-0.0249` n `6`; index avg `0.0099` n `25`; metal avg `0.0977` n `20`; unknown avg `0.0061` n `787`
- 4h: commodity avg `0.2872` n `12`; crypto_alt avg `-0.3221` n `230`; crypto_major avg `-0.3587` n `8`; equity avg `-0.0054` n `113`; fx avg `0.0284` n `6`; index avg `0.0236` n `25`; metal avg `0.1806` n `20`; unknown avg `-0.0026` n `755`
- 24h: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.7648` n `230`; crypto_major avg `-1.0057` n `8`; equity avg `1.2211` n `113`; fx avg `-0.0468` n `6`; index avg `0.2861` n `25`; metal avg `-0.0743` n `20`; unknown avg `0.9641` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2163`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
