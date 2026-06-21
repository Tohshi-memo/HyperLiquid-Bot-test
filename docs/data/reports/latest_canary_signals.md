# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T22:52:28.244502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `0.2203` n `228`; crypto_major avg `0.308` n `8`; equity avg `0.0766` n `78`; fx avg `-0.0013` n `6`; index avg `0.0136` n `23`; metal avg `0.0569` n `18`; unknown avg `0.3699` n `702`
- 1h: commodity avg `-0.2842` n `12`; crypto_alt avg `-0.1336` n `228`; crypto_major avg `-0.0868` n `8`; equity avg `-0.1747` n `78`; fx avg `-0.0058` n `6`; index avg `-0.0464` n `23`; metal avg `0.0611` n `18`; unknown avg `-0.0159` n `702`
- 4h: commodity avg `-0.187` n `12`; crypto_alt avg `-1.2091` n `228`; crypto_major avg `-0.8653` n `8`; equity avg `-0.2701` n `78`; fx avg `-0.0539` n `6`; index avg `-0.0682` n `23`; metal avg `-0.0139` n `18`; unknown avg `0.4135` n `694`
- 24h: commodity avg `0.1124` n `12`; crypto_alt avg `-0.4416` n `228`; crypto_major avg `-1.3578` n `8`; equity avg `-0.1235` n `78`; fx avg `-0.1248` n `6`; index avg `-0.0995` n `23`; metal avg `-0.1251` n `18`; unknown avg `0.4728` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
