# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T11:52:27.129933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `12`; crypto_alt avg `-0.0521` n `230`; crypto_major avg `-0.0384` n `8`; equity avg `0.0746` n `113`; fx avg `0.0043` n `6`; index avg `0.0035` n `25`; metal avg `0.0057` n `20`; unknown avg `-0.0137` n `787`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `-0.024` n `230`; crypto_major avg `-0.0379` n `8`; equity avg `0.2297` n `113`; fx avg `0.0143` n `6`; index avg `0.0254` n `25`; metal avg `0.1013` n `20`; unknown avg `2.4685` n `787`
- 4h: commodity avg `-0.2878` n `12`; crypto_alt avg `-0.0276` n `230`; crypto_major avg `-0.1323` n `8`; equity avg `0.6224` n `113`; fx avg `0.0113` n `6`; index avg `0.0805` n `25`; metal avg `0.1036` n `20`; unknown avg `1.438` n `787`
- 24h: commodity avg `-0.1011` n `12`; crypto_alt avg `-0.4956` n `230`; crypto_major avg `-0.4775` n `8`; equity avg `1.8783` n `113`; fx avg `-0.0285` n `6`; index avg `0.3513` n `25`; metal avg `-0.085` n `20`; unknown avg `0.8481` n `755`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
