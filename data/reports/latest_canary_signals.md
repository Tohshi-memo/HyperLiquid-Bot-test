# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T21:26:31.187108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `0.1431` n `230`; crypto_major avg `-0.0447` n `8`; equity avg `0.0813` n `113`; fx avg `0.0034` n `6`; index avg `0.0075` n `25`; metal avg `0.0235` n `20`; unknown avg `0.0134` n `787`
- 1h: commodity avg `0.0203` n `12`; crypto_alt avg `0.1732` n `230`; crypto_major avg `-0.0032` n `8`; equity avg `0.1479` n `113`; fx avg `-0.0001` n `6`; index avg `0.0227` n `25`; metal avg `0.0331` n `20`; unknown avg `-0.1081` n `787`
- 4h: commodity avg `-0.153` n `12`; crypto_alt avg `0.2943` n `230`; crypto_major avg `0.3063` n `8`; equity avg `-0.1363` n `113`; fx avg `0.0085` n `6`; index avg `-0.0255` n `25`; metal avg `-0.1085` n `20`; unknown avg `-0.0211` n `787`
- 24h: commodity avg `-0.4734` n `12`; crypto_alt avg `-0.1161` n `230`; crypto_major avg `0.2996` n `8`; equity avg `1.5914` n `113`; fx avg `0.027` n `6`; index avg `0.3225` n `25`; metal avg `-0.4565` n `20`; unknown avg `0.0389` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2419`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
