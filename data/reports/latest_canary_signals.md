# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T09:22:29.715122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.2082` n `230`; crypto_major avg `-0.134` n `8`; equity avg `-0.0684` n `96`; fx avg `-0.0018` n `6`; index avg `0.0006` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0154` n `769`
- 1h: commodity avg `0.0206` n `12`; crypto_alt avg `-0.4366` n `230`; crypto_major avg `-0.2868` n `8`; equity avg `-0.0892` n `96`; fx avg `-0.0028` n `6`; index avg `0.0575` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0223` n `769`
- 4h: commodity avg `0.066` n `12`; crypto_alt avg `-0.5613` n `230`; crypto_major avg `-0.2647` n `8`; equity avg `-0.2028` n `96`; fx avg `-0.003` n `6`; index avg `0.0136` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.0748` n `737`
- 24h: commodity avg `0.6535` n `12`; crypto_alt avg `-0.6223` n `230`; crypto_major avg `0.2225` n `8`; equity avg `1.4698` n `96`; fx avg `0.007` n `6`; index avg `0.2894` n `25`; metal avg `0.1568` n `20`; unknown avg `0.2404` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
