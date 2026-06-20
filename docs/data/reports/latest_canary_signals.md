# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T20:07:25.126856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.1109` n `228`; crypto_major avg `0.0708` n `8`; equity avg `0.0252` n `78`; fx avg `0.1847` n `6`; index avg `-0.0097` n `23`; metal avg `0.0115` n `18`; unknown avg `-0.0799` n `701`
- 1h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.1975` n `228`; crypto_major avg `0.2512` n `8`; equity avg `0.1379` n `78`; fx avg `0.002` n `6`; index avg `0.0032` n `23`; metal avg `-0.0179` n `18`; unknown avg `3.466` n `701`
- 4h: commodity avg `-0.022` n `12`; crypto_alt avg `-0.1883` n `228`; crypto_major avg `-0.2706` n `8`; equity avg `0.0081` n `78`; fx avg `-0.0009` n `6`; index avg `0.0031` n `23`; metal avg `-0.0845` n `18`; unknown avg `-0.089` n `701`
- 24h: commodity avg `0.2979` n `12`; crypto_alt avg `0.841` n `228`; crypto_major avg `1.0792` n `8`; equity avg `0.4774` n `78`; fx avg `0.0589` n `6`; index avg `0.052` n `23`; metal avg `-0.0096` n `18`; unknown avg `-0.1618` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
