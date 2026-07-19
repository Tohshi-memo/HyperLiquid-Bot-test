# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T04:37:29.766435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `0.0926` n `230`; crypto_major avg `0.1261` n `8`; equity avg `0.0342` n `96`; fx avg `-0.0098` n `6`; index avg `-0.0024` n `25`; metal avg `0.0112` n `20`; unknown avg `-0.1134` n `770`
- 1h: commodity avg `-0.0488` n `12`; crypto_alt avg `-0.0204` n `230`; crypto_major avg `0.0706` n `8`; equity avg `0.1089` n `96`; fx avg `-0.0094` n `6`; index avg `-0.0227` n `25`; metal avg `-0.0079` n `20`; unknown avg `-0.3323` n `770`
- 4h: commodity avg `-0.0898` n `12`; crypto_alt avg `-0.0185` n `230`; crypto_major avg `0.2122` n `8`; equity avg `0.2201` n `96`; fx avg `-0.0007` n `6`; index avg `0.0088` n `25`; metal avg `0.0394` n `20`; unknown avg `-0.4066` n `770`
- 24h: commodity avg `0.3063` n `12`; crypto_alt avg `0.1173` n `230`; crypto_major avg `0.9114` n `8`; equity avg `-0.0329` n `96`; fx avg `-0.0267` n `6`; index avg `-0.0497` n `25`; metal avg `-0.0136` n `20`; unknown avg `0.0702` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
