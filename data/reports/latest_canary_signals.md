# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T19:52:30.468791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.0185` n `230`; crypto_major avg `-0.023` n `8`; equity avg `-0.1249` n `113`; fx avg `-0.0046` n `6`; index avg `-0.0205` n `25`; metal avg `-0.0157` n `20`; unknown avg `-0.0054` n `787`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `0.0742` n `230`; crypto_major avg `0.1026` n `8`; equity avg `-0.285` n `113`; fx avg `0.0038` n `6`; index avg `-0.0514` n `25`; metal avg `-0.0767` n `20`; unknown avg `0.0615` n `787`
- 4h: commodity avg `-0.316` n `12`; crypto_alt avg `-0.4009` n `230`; crypto_major avg `0.032` n `8`; equity avg `0.1981` n `113`; fx avg `-0.0015` n `6`; index avg `0.0335` n `25`; metal avg `-0.1479` n `20`; unknown avg `-0.0785` n `787`
- 24h: commodity avg `-0.5144` n `12`; crypto_alt avg `-0.2205` n `230`; crypto_major avg `0.4142` n `8`; equity avg `1.1954` n `113`; fx avg `0.0055` n `6`; index avg `0.293` n `25`; metal avg `-0.5295` n `20`; unknown avg `0.0978` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2374`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1827`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
