# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T23:07:18.163282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2412` n `12`; crypto_alt avg `0.0185` n `228`; crypto_major avg `0.0949` n `8`; equity avg `0.1428` n `66`; fx avg `-0.0096` n `6`; index avg `0.0101` n `23`; metal avg `0.089` n `18`; unknown avg `0.1335` n `384`
- 1h: commodity avg `-0.2404` n `12`; crypto_alt avg `0.0189` n `228`; crypto_major avg `0.3541` n `8`; equity avg `0.1504` n `66`; fx avg `0.0036` n `6`; index avg `-0.0039` n `23`; metal avg `-0.0096` n `18`; unknown avg `-0.0281` n `384`
- 4h: commodity avg `-0.122` n `12`; crypto_alt avg `0.1355` n `228`; crypto_major avg `0.5748` n `8`; equity avg `-0.0449` n `66`; fx avg `-0.0669` n `6`; index avg `-0.1285` n `23`; metal avg `-0.2671` n `18`; unknown avg `-0.0901` n `384`
- 24h: commodity avg `-2.6614` n `12`; crypto_alt avg `3.0051` n `228`; crypto_major avg `2.4013` n `8`; equity avg `1.6164` n `66`; fx avg `-0.0751` n `6`; index avg `1.0209` n `23`; metal avg `1.3072` n `18`; unknown avg `1.1609` n `373`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
