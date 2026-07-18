# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T13:52:25.924818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0306` n `12`; crypto_alt avg `-0.0017` n `230`; crypto_major avg `-0.0061` n `8`; equity avg `0.0729` n `96`; fx avg `-0.0006` n `6`; index avg `-0.0082` n `25`; metal avg `0.0038` n `20`; unknown avg `0.0029` n `770`
- 1h: commodity avg `-0.0468` n `12`; crypto_alt avg `-0.2822` n `230`; crypto_major avg `-0.3215` n `8`; equity avg `0.0335` n `96`; fx avg `-0.0011` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0067` n `20`; unknown avg `-0.0436` n `770`
- 4h: commodity avg `0.072` n `12`; crypto_alt avg `-0.1071` n `230`; crypto_major avg `-0.0448` n `8`; equity avg `-0.0314` n `96`; fx avg `-0.0075` n `6`; index avg `-0.0107` n `25`; metal avg `-0.017` n `20`; unknown avg `-0.0861` n `769`
- 24h: commodity avg `0.3471` n `12`; crypto_alt avg `-0.2139` n `230`; crypto_major avg `0.6735` n `8`; equity avg `1.3712` n `96`; fx avg `0.0233` n `6`; index avg `0.2679` n `25`; metal avg `0.2945` n `20`; unknown avg `0.0462` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
