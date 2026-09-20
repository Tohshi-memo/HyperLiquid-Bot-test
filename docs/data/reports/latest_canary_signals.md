# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T22:22:31.007692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `0.0136` n `234`; crypto_major avg `0.0163` n `8`; equity avg `0.0749` n `140`; fx avg `0.025` n `6`; index avg `0.0371` n `26`; metal avg `-0.0048` n `20`; unknown avg `2.2183` n `927`
- 1h: commodity avg `-0.2393` n `12`; crypto_alt avg `0.6184` n `234`; crypto_major avg `0.4393` n `8`; equity avg `0.2281` n `140`; fx avg `0.0763` n `6`; index avg `0.0481` n `26`; metal avg `0.0847` n `20`; unknown avg `3.0569` n `913`
- 4h: commodity avg `-0.2175` n `12`; crypto_alt avg `0.5845` n `234`; crypto_major avg `0.1287` n `8`; equity avg `0.2739` n `140`; fx avg `0.0363` n `6`; index avg `0.0625` n `26`; metal avg `0.0567` n `20`; unknown avg `1.5764` n `845`
- 24h: commodity avg `0.0875` n `12`; crypto_alt avg `1.9571` n `234`; crypto_major avg `0.7292` n `8`; equity avg `0.1311` n `140`; fx avg `0.04` n `6`; index avg `0.0122` n `26`; metal avg `0.0196` n `20`; unknown avg `2.9298` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
