# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T19:22:23.586434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `-0.0213` n `230`; crypto_major avg `0.0295` n `8`; equity avg `0.0348` n `114`; fx avg `0.0006` n `6`; index avg `0.0084` n `25`; metal avg `0.0036` n `20`; unknown avg `0.0012` n `791`
- 1h: commodity avg `0.0357` n `12`; crypto_alt avg `0.0361` n `230`; crypto_major avg `0.0892` n `8`; equity avg `0.0531` n `114`; fx avg `0.0028` n `6`; index avg `0.0046` n `25`; metal avg `-0.0047` n `20`; unknown avg `0.5082` n `791`
- 4h: commodity avg `0.0802` n `12`; crypto_alt avg `0.0262` n `230`; crypto_major avg `0.1404` n `8`; equity avg `0.0649` n `114`; fx avg `-0.0003` n `6`; index avg `0.0142` n `25`; metal avg `0.004` n `20`; unknown avg `0.0755` n `791`
- 24h: commodity avg `-0.0016` n `12`; crypto_alt avg `1.061` n `230`; crypto_major avg `0.6838` n `8`; equity avg `0.478` n `114`; fx avg `0.0218` n `6`; index avg `0.041` n `25`; metal avg `0.0549` n `20`; unknown avg `0.0899` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
