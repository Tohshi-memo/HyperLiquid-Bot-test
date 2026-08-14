# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T07:37:32.504614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `12`; crypto_alt avg `-0.1311` n `230`; crypto_major avg `-0.0651` n `8`; equity avg `0.0071` n `113`; fx avg `-0.0035` n `6`; index avg `0.0023` n `25`; metal avg `0.0586` n `20`; unknown avg `0.0425` n `787`
- 1h: commodity avg `0.0831` n `12`; crypto_alt avg `-0.2972` n `230`; crypto_major avg `-0.1283` n `8`; equity avg `0.0635` n `113`; fx avg `0.0021` n `6`; index avg `0.012` n `25`; metal avg `0.0549` n `20`; unknown avg `0.1072` n `787`
- 4h: commodity avg `0.243` n `12`; crypto_alt avg `-0.4383` n `230`; crypto_major avg `-0.4563` n `8`; equity avg `-0.1134` n `113`; fx avg `0.069` n `6`; index avg `0.0113` n `25`; metal avg `0.0774` n `20`; unknown avg `-0.0081` n `755`
- 24h: commodity avg `-0.0495` n `12`; crypto_alt avg `-0.9041` n `230`; crypto_major avg `-1.0605` n `8`; equity avg `1.1988` n `113`; fx avg `-0.0091` n `6`; index avg `0.2736` n `25`; metal avg `-0.1916` n `20`; unknown avg `0.9182` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2173`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
