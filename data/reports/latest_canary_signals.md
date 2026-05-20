# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T08:52:15.892052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.342` n `12`; crypto_alt avg `-0.0147` n `228`; crypto_major avg `0.0124` n `8`; equity avg `0.0945` n `66`; fx avg `-0.0167` n `6`; index avg `0.0397` n `23`; metal avg `0.207` n `18`; unknown avg `0.5726` n `384`
- 1h: commodity avg `-0.4719` n `12`; crypto_alt avg `0.1472` n `228`; crypto_major avg `0.2244` n `8`; equity avg `0.3932` n `66`; fx avg `-0.0298` n `6`; index avg `0.2504` n `23`; metal avg `0.3803` n `18`; unknown avg `0.4432` n `384`
- 4h: commodity avg `-0.7811` n `12`; crypto_alt avg `0.9923` n `228`; crypto_major avg `0.8597` n `8`; equity avg `0.9264` n `66`; fx avg `-0.0891` n `6`; index avg `0.5287` n `23`; metal avg `1.1719` n `18`; unknown avg `1.003` n `374`
- 24h: commodity avg `-0.2465` n `12`; crypto_alt avg `0.0281` n `228`; crypto_major avg `-0.082` n `8`; equity avg `0.7825` n `66`; fx avg `-0.1889` n `6`; index avg `-0.1116` n `23`; metal avg `-0.8131` n `18`; unknown avg `0.8192` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
