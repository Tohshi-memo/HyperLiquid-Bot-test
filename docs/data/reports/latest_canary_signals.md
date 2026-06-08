# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T19:07:27.577775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `0.1492` n `228`; crypto_major avg `0.114` n `8`; equity avg `-0.1423` n `74`; fx avg `-0.0192` n `6`; index avg `-0.057` n `23`; metal avg `0.0159` n `18`; unknown avg `0.0551` n `517`
- 1h: commodity avg `-0.1558` n `12`; crypto_alt avg `-0.2293` n `228`; crypto_major avg `-0.0772` n `8`; equity avg `-0.3885` n `74`; fx avg `-0.0264` n `6`; index avg `-0.1625` n `23`; metal avg `-0.1295` n `18`; unknown avg `0.0253` n `517`
- 4h: commodity avg `-0.077` n `12`; crypto_alt avg `0.1176` n `228`; crypto_major avg `-0.095` n `8`; equity avg `-0.6395` n `74`; fx avg `-0.0392` n `6`; index avg `-0.4266` n `23`; metal avg `-0.0904` n `18`; unknown avg `0.0089` n `517`
- 24h: commodity avg `-1.1832` n `12`; crypto_alt avg `3.8668` n `228`; crypto_major avg `4.1011` n `8`; equity avg `2.5272` n `74`; fx avg `-0.3039` n `6`; index avg `1.1308` n `23`; metal avg `0.087` n `18`; unknown avg `-1.7849` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
