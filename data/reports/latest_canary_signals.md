# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T10:22:30.869499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0506` n `12`; crypto_alt avg `-0.2385` n `230`; crypto_major avg `-0.1733` n `8`; equity avg `0.0745` n `113`; fx avg `-0.0119` n `6`; index avg `0.02` n `25`; metal avg `0.02` n `20`; unknown avg `0.0125` n `785`
- 1h: commodity avg `-0.1016` n `12`; crypto_alt avg `-0.2454` n `230`; crypto_major avg `-0.0552` n `8`; equity avg `0.1347` n `113`; fx avg `-0.0153` n `6`; index avg `0.0289` n `25`; metal avg `0.0508` n `20`; unknown avg `-0.0571` n `785`
- 4h: commodity avg `0.1661` n `12`; crypto_alt avg `-0.364` n `230`; crypto_major avg `0.1205` n `8`; equity avg `-0.1029` n `113`; fx avg `-0.016` n `6`; index avg `0.0122` n `25`; metal avg `0.1655` n `20`; unknown avg `-0.0038` n `785`
- 24h: commodity avg `1.0939` n `12`; crypto_alt avg `-1.3026` n `230`; crypto_major avg `-0.6723` n `8`; equity avg `-1.3139` n `113`; fx avg `0.0014` n `6`; index avg `-0.0106` n `25`; metal avg `0.3589` n `20`; unknown avg `0.1517` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
