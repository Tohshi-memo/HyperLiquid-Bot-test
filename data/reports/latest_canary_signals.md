# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T19:22:26.845241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `-0.0188` n `228`; crypto_major avg `0.0732` n `8`; equity avg `0.0647` n `78`; fx avg `-0.0011` n `6`; index avg `0.0026` n `23`; metal avg `0.0098` n `18`; unknown avg `0.1423` n `701`
- 1h: commodity avg `-0.0359` n `12`; crypto_alt avg `-0.1707` n `228`; crypto_major avg `-0.0097` n `8`; equity avg `0.0478` n `78`; fx avg `-0.003` n `6`; index avg `0.0048` n `23`; metal avg `0.0274` n `18`; unknown avg `-0.238` n `701`
- 4h: commodity avg `-0.023` n `12`; crypto_alt avg `-0.5522` n `228`; crypto_major avg `-0.7525` n `8`; equity avg `-0.1763` n `78`; fx avg `0.0345` n `6`; index avg `-0.0106` n `23`; metal avg `-0.0932` n `18`; unknown avg `0.1691` n `701`
- 24h: commodity avg `0.3039` n `12`; crypto_alt avg `0.7534` n `228`; crypto_major avg `0.9433` n `8`; equity avg `0.3911` n `78`; fx avg `0.0621` n `6`; index avg `0.0456` n `23`; metal avg `0.0955` n `18`; unknown avg `-0.0054` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
