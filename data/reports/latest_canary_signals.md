# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T12:52:39.486703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0827` n `12`; crypto_alt avg `-0.1189` n `230`; crypto_major avg `-0.2463` n `8`; equity avg `0.0564` n `113`; fx avg `0.015` n `6`; index avg `0.0478` n `25`; metal avg `-0.0447` n `20`; unknown avg `0.0232` n `786`
- 1h: commodity avg `-0.0397` n `12`; crypto_alt avg `0.1208` n `230`; crypto_major avg `-0.2414` n `8`; equity avg `0.6059` n `113`; fx avg `0.0055` n `6`; index avg `0.0922` n `25`; metal avg `-0.0658` n `20`; unknown avg `-0.0758` n `786`
- 4h: commodity avg `0.0232` n `12`; crypto_alt avg `0.6453` n `230`; crypto_major avg `0.4401` n `8`; equity avg `0.8968` n `113`; fx avg `0.0076` n `6`; index avg `0.1308` n `25`; metal avg `0.1908` n `20`; unknown avg `-0.0609` n `786`
- 24h: commodity avg `0.1048` n `12`; crypto_alt avg `-0.6607` n `230`; crypto_major avg `0.6832` n `8`; equity avg `3.0017` n `113`; fx avg `0.0617` n `6`; index avg `0.2936` n `25`; metal avg `0.341` n `20`; unknown avg `-0.1243` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2469`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2357`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2117`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
