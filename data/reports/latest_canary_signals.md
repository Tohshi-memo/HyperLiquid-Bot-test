# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T01:52:15.611803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0411` n `12`; crypto_alt avg `0.0743` n `228`; crypto_major avg `0.0824` n `8`; equity avg `0.0332` n `66`; fx avg `0.0106` n `6`; index avg `0.0226` n `23`; metal avg `-0.0367` n `18`; unknown avg `0.8501` n `384`
- 1h: commodity avg `-0.2306` n `12`; crypto_alt avg `0.1464` n `228`; crypto_major avg `0.125` n `8`; equity avg `0.2491` n `66`; fx avg `0.047` n `6`; index avg `0.1576` n `23`; metal avg `0.4211` n `18`; unknown avg `1.604` n `384`
- 4h: commodity avg `-0.4015` n `12`; crypto_alt avg `0.7374` n `228`; crypto_major avg `1.2363` n `8`; equity avg `0.5372` n `66`; fx avg `0.0828` n `6`; index avg `0.1842` n `23`; metal avg `0.4334` n `18`; unknown avg `4.0619` n `384`
- 24h: commodity avg `-2.1927` n `12`; crypto_alt avg `3.7172` n `228`; crypto_major avg `3.8291` n `8`; equity avg `2.3432` n `66`; fx avg `0.0386` n `6`; index avg `1.4896` n `23`; metal avg `2.0274` n `18`; unknown avg `5.5109` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
