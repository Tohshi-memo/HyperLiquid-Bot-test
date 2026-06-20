# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T20:22:30.661825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `-0.117` n `228`; crypto_major avg `-0.006` n `8`; equity avg `0.0353` n `78`; fx avg `-0.0039` n `6`; index avg `-0.0001` n `23`; metal avg `-0.0015` n `18`; unknown avg `-0.2879` n `701`
- 1h: commodity avg `-0.0228` n `12`; crypto_alt avg `0.1002` n `228`; crypto_major avg `0.1718` n `8`; equity avg `0.1084` n `78`; fx avg `-0.0008` n `6`; index avg `0.0005` n `23`; metal avg `-0.0291` n `18`; unknown avg `0.6704` n `701`
- 4h: commodity avg `-0.0335` n `12`; crypto_alt avg `-0.2291` n `228`; crypto_major avg `-0.21` n `8`; equity avg `0.0059` n `78`; fx avg `-0.0048` n `6`; index avg `-0.0132` n `23`; metal avg `-0.086` n `18`; unknown avg `-0.0856` n `701`
- 24h: commodity avg `0.3085` n `12`; crypto_alt avg `0.915` n `228`; crypto_major avg `1.3904` n `8`; equity avg `0.5291` n `78`; fx avg `0.0643` n `6`; index avg `0.054` n `23`; metal avg `-0.0095` n `18`; unknown avg `-0.1908` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
