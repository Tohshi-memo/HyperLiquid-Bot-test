# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T19:52:28.863199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.015` n `228`; crypto_major avg `0.0596` n `8`; equity avg `0.0209` n `78`; fx avg `-0.1803` n `6`; index avg `0.0053` n `23`; metal avg `-0.0083` n `18`; unknown avg `1.3589` n `701`
- 1h: commodity avg `-0.0243` n `12`; crypto_alt avg `-0.0255` n `228`; crypto_major avg `0.0922` n `8`; equity avg `0.1048` n `78`; fx avg `-0.1826` n `6`; index avg `0.0164` n `23`; metal avg `-0.0265` n `18`; unknown avg `3.459` n `701`
- 4h: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.3431` n `228`; crypto_major avg `-0.4467` n `8`; equity avg `-0.043` n `78`; fx avg `-0.159` n `6`; index avg `-0.0002` n `23`; metal avg `-0.1109` n `18`; unknown avg `0.0624` n `701`
- 24h: commodity avg `0.3066` n `12`; crypto_alt avg `0.8054` n `228`; crypto_major avg `1.021` n `8`; equity avg `0.4605` n `78`; fx avg `-0.1245` n `6`; index avg `0.0662` n `23`; metal avg `0.032` n `18`; unknown avg `-0.0558` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
