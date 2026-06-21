# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T00:07:29.097938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `0.0213` n `228`; crypto_major avg `-0.0796` n `8`; equity avg `-0.0102` n `78`; fx avg `-0.1223` n `6`; index avg `0.0015` n `23`; metal avg `-0.0135` n `18`; unknown avg `0.2037` n `701`
- 1h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0024` n `228`; crypto_major avg `-0.1747` n `8`; equity avg `-0.045` n `78`; fx avg `-0.1245` n `6`; index avg `-0.0259` n `23`; metal avg `-0.0201` n `18`; unknown avg `0.2559` n `701`
- 4h: commodity avg `0.035` n `12`; crypto_alt avg `0.5212` n `228`; crypto_major avg `0.5919` n `8`; equity avg `0.1439` n `78`; fx avg `-0.1217` n `6`; index avg `0.0142` n `23`; metal avg `0.0095` n `18`; unknown avg `-0.525` n `701`
- 24h: commodity avg `0.2348` n `12`; crypto_alt avg `0.8094` n `228`; crypto_major avg `1.3164` n `8`; equity avg `0.3198` n `78`; fx avg `-0.0648` n `6`; index avg `0.0127` n `23`; metal avg `-0.0522` n `18`; unknown avg `-0.47` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
