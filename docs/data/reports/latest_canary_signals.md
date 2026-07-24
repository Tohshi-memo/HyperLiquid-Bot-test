# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T11:52:29.765103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1025` n `12`; crypto_alt avg `-0.0121` n `230`; crypto_major avg `-0.0026` n `8`; equity avg `-0.0331` n `100`; fx avg `-0.0075` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0388` n `20`; unknown avg `0.0047` n `773`
- 1h: commodity avg `0.0116` n `12`; crypto_alt avg `-0.1495` n `230`; crypto_major avg `-0.2069` n `8`; equity avg `-0.0568` n `100`; fx avg `-0.0151` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0442` n `20`; unknown avg `-0.0127` n `773`
- 4h: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.6932` n `230`; crypto_major avg `-0.6641` n `8`; equity avg `-0.0345` n `100`; fx avg `-0.0737` n `6`; index avg `0.0156` n `25`; metal avg `0.073` n `20`; unknown avg `0.0611` n `772`
- 24h: commodity avg `-0.1657` n `12`; crypto_alt avg `-1.4804` n `230`; crypto_major avg `-1.9317` n `8`; equity avg `-1.4177` n `99`; fx avg `-0.1545` n `6`; index avg `-0.3635` n `25`; metal avg `-0.2971` n `20`; unknown avg `0.1554` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1005`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0889`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0843`, n `666`, weak_sample_signal
