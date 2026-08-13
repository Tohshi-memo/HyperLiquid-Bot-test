# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T02:37:30.190174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `-0.1096` n `230`; crypto_major avg `-0.0655` n `8`; equity avg `-0.1263` n `113`; fx avg `-0.0002` n `6`; index avg `-0.0329` n `25`; metal avg `-0.1128` n `20`; unknown avg `0.0066` n `786`
- 1h: commodity avg `-0.0278` n `12`; crypto_alt avg `-0.1733` n `230`; crypto_major avg `-0.111` n `8`; equity avg `0.1011` n `113`; fx avg `0.0148` n `6`; index avg `0.0006` n `25`; metal avg `-0.2275` n `20`; unknown avg `-0.2262` n `786`
- 4h: commodity avg `-0.1174` n `12`; crypto_alt avg `0.307` n `230`; crypto_major avg `0.1574` n `8`; equity avg `0.5246` n `113`; fx avg `-0.0339` n `6`; index avg `0.044` n `25`; metal avg `-0.0501` n `20`; unknown avg `-0.2546` n `786`
- 24h: commodity avg `-0.2759` n `12`; crypto_alt avg `-1.5915` n `230`; crypto_major avg `-0.5758` n `8`; equity avg `2.5087` n `113`; fx avg `-0.0588` n `6`; index avg `0.2809` n `25`; metal avg `-0.1634` n `20`; unknown avg `-0.0176` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2379`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2015`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
