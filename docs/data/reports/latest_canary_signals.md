# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T17:07:30.645897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0584` n `12`; crypto_alt avg `0.0077` n `230`; crypto_major avg `0.0806` n `8`; equity avg `0.1137` n `113`; fx avg `0.0073` n `6`; index avg `0.013` n `25`; metal avg `0.0189` n `20`; unknown avg `0.0068` n `785`
- 1h: commodity avg `0.1283` n `12`; crypto_alt avg `-0.1894` n `230`; crypto_major avg `-0.2512` n `8`; equity avg `-0.1726` n `113`; fx avg `-0.003` n `6`; index avg `-0.0362` n `25`; metal avg `-0.0853` n `20`; unknown avg `-0.0639` n `785`
- 4h: commodity avg `0.4694` n `12`; crypto_alt avg `-0.7751` n `230`; crypto_major avg `-0.8866` n `8`; equity avg `-0.3049` n `113`; fx avg `0.0203` n `6`; index avg `0.0003` n `25`; metal avg `0.2001` n `20`; unknown avg `1.6479` n `784`
- 24h: commodity avg `1.2265` n `12`; crypto_alt avg `-0.9064` n `230`; crypto_major avg `-1.6447` n `8`; equity avg `-1.2309` n `113`; fx avg `0.2399` n `6`; index avg `-0.053` n `25`; metal avg `-0.0265` n `20`; unknown avg `103.361` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
