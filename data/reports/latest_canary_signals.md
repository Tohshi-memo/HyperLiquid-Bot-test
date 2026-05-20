# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T14:52:25.326605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `12`; crypto_alt avg `0.1365` n `228`; crypto_major avg `0.323` n `8`; equity avg `0.1437` n `66`; fx avg `-0.0293` n `6`; index avg `0.0741` n `23`; metal avg `0.1429` n `18`; unknown avg `-0.1688` n `384`
- 1h: commodity avg `-0.8314` n `12`; crypto_alt avg `0.9833` n `228`; crypto_major avg `0.6341` n `8`; equity avg `0.5667` n `66`; fx avg `-0.0282` n `6`; index avg `0.4063` n `23`; metal avg `0.9765` n `18`; unknown avg `0.3047` n `384`
- 4h: commodity avg `-0.7121` n `12`; crypto_alt avg `0.8402` n `228`; crypto_major avg `0.7323` n `8`; equity avg `0.3373` n `66`; fx avg `0.0082` n `6`; index avg `0.6938` n `23`; metal avg `0.4807` n `18`; unknown avg `1.3398` n `384`
- 24h: commodity avg `-1.4121` n `12`; crypto_alt avg `2.5292` n `228`; crypto_major avg `2.1221` n `8`; equity avg `2.7066` n `66`; fx avg `-0.1129` n `6`; index avg `1.6579` n `23`; metal avg `1.312` n `18`; unknown avg `1.2516` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
