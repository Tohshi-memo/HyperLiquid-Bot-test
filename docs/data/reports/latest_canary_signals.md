# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T10:13:57.867531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0829` n `12`; crypto_alt avg `0.0603` n `230`; crypto_major avg `0.0226` n `8`; equity avg `0.1422` n `113`; fx avg `0.0253` n `6`; index avg `0.0255` n `25`; metal avg `0.001` n `20`; unknown avg `0.1687` n `787`
- 1h: commodity avg `-0.1208` n `12`; crypto_alt avg `-0.2241` n `230`; crypto_major avg `-0.1709` n `8`; equity avg `0.2487` n `113`; fx avg `0.0056` n `6`; index avg `0.0441` n `25`; metal avg `0.0398` n `20`; unknown avg `0.0244` n `787`
- 4h: commodity avg `-0.1167` n `12`; crypto_alt avg `-0.4656` n `230`; crypto_major avg `-0.4127` n `8`; equity avg `0.5695` n `113`; fx avg `0.026` n `6`; index avg `0.0742` n `25`; metal avg `0.1415` n `20`; unknown avg `-0.0555` n `787`
- 24h: commodity avg `-0.1422` n `12`; crypto_alt avg `-0.899` n `230`; crypto_major avg `-0.8111` n `8`; equity avg `1.7713` n `113`; fx avg `-0.0683` n `6`; index avg `0.3598` n `25`; metal avg `-0.1081` n `20`; unknown avg `0.9736` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
