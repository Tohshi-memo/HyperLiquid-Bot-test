# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T07:47:00.895195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `-0.0619` n `230`; crypto_major avg `-0.0441` n `8`; equity avg `0.011` n `113`; fx avg `-0.0081` n `6`; index avg `0.0074` n `25`; metal avg `0.0354` n `20`; unknown avg `-0.0657` n `787`
- 1h: commodity avg `0.0919` n `12`; crypto_alt avg `-0.2214` n `230`; crypto_major avg `-0.0675` n `8`; equity avg `0.0004` n `113`; fx avg `-0.0056` n `6`; index avg `0.0095` n `25`; metal avg `0.0682` n `20`; unknown avg `-0.0418` n `787`
- 4h: commodity avg `0.2739` n `12`; crypto_alt avg `-0.379` n `230`; crypto_major avg `-0.3734` n `8`; equity avg `-0.0591` n `113`; fx avg `0.0478` n `6`; index avg `0.0231` n `25`; metal avg `0.1511` n `20`; unknown avg `-0.0569` n `755`
- 24h: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.8215` n `230`; crypto_major avg `-1.0203` n `8`; equity avg `1.1665` n `113`; fx avg `-0.0276` n `6`; index avg `0.2856` n `25`; metal avg `-0.1035` n `20`; unknown avg `0.9008` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2161`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
