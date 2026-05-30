# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T11:52:20.133296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0189` n `12`; crypto_alt avg `-0.1011` n `228`; crypto_major avg `0.0189` n `8`; equity avg `0.0848` n `69`; fx avg `0.0026` n `6`; index avg `0.0006` n `23`; metal avg `-0.0012` n `18`; unknown avg `-0.1667` n `421`
- 1h: commodity avg `0.0262` n `12`; crypto_alt avg `-0.1429` n `228`; crypto_major avg `0.0507` n `8`; equity avg `0.0111` n `69`; fx avg `-0.0023` n `6`; index avg `0.0048` n `23`; metal avg `-0.0202` n `18`; unknown avg `-0.2363` n `421`
- 4h: commodity avg `0.0341` n `12`; crypto_alt avg `0.0654` n `228`; crypto_major avg `0.3414` n `8`; equity avg `0.0797` n `69`; fx avg `0.0203` n `6`; index avg `-0.0585` n `23`; metal avg `0.0257` n `18`; unknown avg `-0.1702` n `421`
- 24h: commodity avg `-0.3278` n `12`; crypto_alt avg `1.9799` n `228`; crypto_major avg `2.5215` n `8`; equity avg `1.317` n `69`; fx avg `0.1062` n `6`; index avg `-0.0597` n `23`; metal avg `-0.1679` n `18`; unknown avg `0.5385` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1922`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
