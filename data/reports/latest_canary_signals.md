# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T18:52:27.688140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0146` n `12`; crypto_alt avg `0.0218` n `228`; crypto_major avg `-0.0303` n `8`; equity avg `-0.0079` n `78`; fx avg `0.0` n `6`; index avg `-0.0019` n `23`; metal avg `0.0017` n `18`; unknown avg `-0.3165` n `701`
- 1h: commodity avg `0.0018` n `12`; crypto_alt avg `0.151` n `228`; crypto_major avg `0.1647` n `8`; equity avg `-0.0146` n `78`; fx avg `-0.0028` n `6`; index avg `-0.0128` n `23`; metal avg `0.0084` n `18`; unknown avg `-0.3053` n `701`
- 4h: commodity avg `0.0744` n `12`; crypto_alt avg `-0.0023` n `228`; crypto_major avg `-0.4226` n `8`; equity avg `-0.1411` n `78`; fx avg `0.0212` n `6`; index avg `-0.0127` n `23`; metal avg `-0.0914` n `18`; unknown avg `0.1299` n `701`
- 24h: commodity avg `0.3025` n `12`; crypto_alt avg `0.5791` n `228`; crypto_major avg `0.9419` n `8`; equity avg `0.3375` n `78`; fx avg `0.0637` n `6`; index avg `0.0616` n `23`; metal avg `0.0958` n `18`; unknown avg `0.0226` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
