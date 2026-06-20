# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T21:07:33.673342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0372` n `12`; crypto_alt avg `0.0037` n `228`; crypto_major avg `0.0426` n `8`; equity avg `0.0022` n `78`; fx avg `0.0013` n `6`; index avg `-0.0016` n `23`; metal avg `0.0159` n `18`; unknown avg `-0.0481` n `701`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `-0.182` n `228`; crypto_major avg `0.038` n `8`; equity avg `0.0513` n `78`; fx avg `0.0` n `6`; index avg `-0.0058` n `23`; metal avg `0.0194` n `18`; unknown avg `-0.0088` n `701`
- 4h: commodity avg `-0.0715` n `12`; crypto_alt avg `-0.2937` n `228`; crypto_major avg `0.1207` n `8`; equity avg `0.1247` n `78`; fx avg `-0.0042` n `6`; index avg `-0.0018` n `23`; metal avg `-0.0111` n `18`; unknown avg `0.088` n `701`
- 24h: commodity avg `0.2859` n `12`; crypto_alt avg `0.5349` n `228`; crypto_major avg `1.074` n `8`; equity avg `0.5078` n `78`; fx avg `0.0983` n `6`; index avg `0.0663` n `23`; metal avg `-0.0531` n `18`; unknown avg `0.052` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
