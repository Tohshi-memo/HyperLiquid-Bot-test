# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T01:37:23.994340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.1458` n `228`; crypto_major avg `0.1355` n `8`; equity avg `0.0081` n `69`; fx avg `-0.0148` n `6`; index avg `-0.0155` n `23`; metal avg `-0.0074` n `18`; unknown avg `0.1903` n `421`
- 1h: commodity avg `0.1514` n `12`; crypto_alt avg `0.4477` n `228`; crypto_major avg `0.4679` n `8`; equity avg `0.0959` n `69`; fx avg `-0.0149` n `6`; index avg `0.0251` n `23`; metal avg `0.0053` n `18`; unknown avg `0.6308` n `421`
- 4h: commodity avg `0.1198` n `12`; crypto_alt avg `-0.2213` n `228`; crypto_major avg `0.4278` n `8`; equity avg `0.1735` n `69`; fx avg `-0.0228` n `6`; index avg `0.0197` n `23`; metal avg `-0.0078` n `18`; unknown avg `-0.0975` n `421`
- 24h: commodity avg `-0.1828` n `12`; crypto_alt avg `0.4023` n `228`; crypto_major avg `2.4107` n `8`; equity avg `0.969` n `69`; fx avg `0.0091` n `6`; index avg `0.0662` n `23`; metal avg `0.0055` n `18`; unknown avg `0.5386` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
