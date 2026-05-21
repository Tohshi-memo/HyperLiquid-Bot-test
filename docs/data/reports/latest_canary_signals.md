# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T02:07:17.402825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0326` n `12`; crypto_alt avg `-0.0718` n `228`; crypto_major avg `-0.194` n `8`; equity avg `-0.0035` n `66`; fx avg `-0.001` n `6`; index avg `0.0021` n `23`; metal avg `-0.1132` n `18`; unknown avg `-0.1898` n `384`
- 1h: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.033` n `228`; crypto_major avg `-0.1323` n `8`; equity avg `0.1851` n `66`; fx avg `0.0182` n `6`; index avg `0.1345` n `23`; metal avg `0.3165` n `18`; unknown avg `0.8639` n `384`
- 4h: commodity avg `-0.0889` n `12`; crypto_alt avg `0.9487` n `228`; crypto_major avg `1.3203` n `8`; equity avg `0.8177` n `66`; fx avg `0.0795` n `6`; index avg `0.3515` n `23`; metal avg `0.3963` n `18`; unknown avg `3.2016` n `384`
- 24h: commodity avg `-2.1917` n `12`; crypto_alt avg `3.4969` n `228`; crypto_major avg `3.4702` n `8`; equity avg `2.1992` n `66`; fx avg `0.0551` n `6`; index avg `1.4415` n `23`; metal avg `1.8333` n `18`; unknown avg `4.4966` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
