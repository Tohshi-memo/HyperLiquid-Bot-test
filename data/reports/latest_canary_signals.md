# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T21:52:30.740921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0406` n `12`; crypto_alt avg `-0.0466` n `228`; crypto_major avg `0.0022` n `8`; equity avg `0.0173` n `78`; fx avg `0.0024` n `6`; index avg `0.0041` n `23`; metal avg `-0.0029` n `18`; unknown avg `-0.078` n `701`
- 1h: commodity avg `0.0562` n `12`; crypto_alt avg `0.2195` n `228`; crypto_major avg `0.2294` n `8`; equity avg `0.0194` n `78`; fx avg `-0.0076` n `6`; index avg `0.0064` n `23`; metal avg `0.0025` n `18`; unknown avg `0.0434` n `701`
- 4h: commodity avg `0.0018` n `12`; crypto_alt avg `0.2695` n `228`; crypto_major avg `0.5539` n `8`; equity avg `0.184` n `78`; fx avg `-0.0115` n `6`; index avg `-0.0039` n `23`; metal avg `-0.0006` n `18`; unknown avg `0.1256` n `701`
- 24h: commodity avg `0.0308` n `12`; crypto_alt avg `1.0773` n `228`; crypto_major avg `1.6194` n `8`; equity avg `0.5813` n `78`; fx avg `0.1238` n `6`; index avg `0.0739` n `23`; metal avg `-0.0517` n `18`; unknown avg `0.1755` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
