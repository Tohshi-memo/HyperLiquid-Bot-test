# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T10:07:35.698048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0823` n `12`; crypto_alt avg `0.0063` n `230`; crypto_major avg `0.0201` n `8`; equity avg `0.1612` n `113`; fx avg `0.0261` n `6`; index avg `0.0189` n `25`; metal avg `0.0139` n `20`; unknown avg `0.1738` n `787`
- 1h: commodity avg `-0.1202` n `12`; crypto_alt avg `-0.2769` n `230`; crypto_major avg `-0.1734` n `8`; equity avg `0.2679` n `113`; fx avg `0.0064` n `6`; index avg `0.0375` n `25`; metal avg `0.0526` n `20`; unknown avg `0.0286` n `787`
- 4h: commodity avg `-0.1161` n `12`; crypto_alt avg `-0.5167` n `230`; crypto_major avg `-0.4152` n `8`; equity avg `0.589` n `113`; fx avg `0.0268` n `6`; index avg `0.0676` n `25`; metal avg `0.1545` n `20`; unknown avg `-0.0563` n `787`
- 24h: commodity avg `-0.1416` n `12`; crypto_alt avg `-0.9469` n `230`; crypto_major avg `-0.8134` n `8`; equity avg `1.7922` n `113`; fx avg `-0.0675` n `6`; index avg `0.353` n `25`; metal avg `-0.0953` n `20`; unknown avg `0.9726` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
