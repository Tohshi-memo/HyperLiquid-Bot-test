# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T04:22:25.168591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0171` n `12`; crypto_alt avg `0.0159` n `228`; crypto_major avg `0.1429` n `8`; equity avg `0.0218` n `78`; fx avg `0.0978` n `6`; index avg `0.0052` n `23`; metal avg `0.0006` n `18`; unknown avg `0.0806` n `702`
- 1h: commodity avg `0.026` n `12`; crypto_alt avg `-0.164` n `228`; crypto_major avg `-0.1292` n `8`; equity avg `0.0786` n `78`; fx avg `-0.0042` n `6`; index avg `0.0002` n `23`; metal avg `0.0` n `18`; unknown avg `-0.3954` n `702`
- 4h: commodity avg `0.0241` n `12`; crypto_alt avg `0.0694` n `228`; crypto_major avg `0.0586` n `8`; equity avg `0.1426` n `78`; fx avg `-0.0091` n `6`; index avg `0.0182` n `23`; metal avg `0.0153` n `18`; unknown avg `0.8489` n `701`
- 24h: commodity avg `0.2308` n `12`; crypto_alt avg `1.5093` n `228`; crypto_major avg `1.5917` n `8`; equity avg `0.3997` n `78`; fx avg `0.041` n `6`; index avg `0.016` n `23`; metal avg `-0.0153` n `18`; unknown avg `1.8414` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
