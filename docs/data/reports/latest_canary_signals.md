# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T08:26:01.484098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `0.0931` n `230`; crypto_major avg `0.1071` n `8`; equity avg `-0.0009` n `96`; fx avg `-0.0027` n `6`; index avg `-0.0046` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.0341` n `769`
- 1h: commodity avg `0.017` n `12`; crypto_alt avg `0.0718` n `230`; crypto_major avg `0.1008` n `8`; equity avg `-0.0247` n `96`; fx avg `0.0013` n `6`; index avg `0.0071` n `25`; metal avg `0.0139` n `20`; unknown avg `-0.0463` n `769`
- 4h: commodity avg `0.0605` n `12`; crypto_alt avg `-0.2197` n `230`; crypto_major avg `0.0029` n `8`; equity avg `-0.1398` n `96`; fx avg `0.0003` n `6`; index avg `-0.0198` n `25`; metal avg `0.0147` n `20`; unknown avg `-0.0814` n `737`
- 24h: commodity avg `0.8458` n `12`; crypto_alt avg `0.1421` n `230`; crypto_major avg `0.812` n `8`; equity avg `1.8681` n `96`; fx avg `0.0274` n `6`; index avg `0.2602` n `25`; metal avg `0.3191` n `20`; unknown avg `0.2882` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
