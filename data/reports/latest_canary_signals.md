# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T23:58:13.422620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.024` n `12`; crypto_alt avg `0.0085` n `228`; crypto_major avg `0.1835` n `8`; equity avg `0.062` n `66`; fx avg `0.0311` n `6`; index avg `0.0559` n `23`; metal avg `0.0927` n `18`; unknown avg `2.0824` n `384`
- 1h: commodity avg `-0.0261` n `12`; crypto_alt avg `0.0905` n `228`; crypto_major avg `0.3631` n `8`; equity avg `0.0686` n `66`; fx avg `0.0229` n `6`; index avg `0.0331` n `23`; metal avg `0.1859` n `18`; unknown avg `2.4406` n `384`
- 4h: commodity avg `0.0643` n `12`; crypto_alt avg `-0.3158` n `228`; crypto_major avg `0.3244` n `8`; equity avg `-0.2116` n `66`; fx avg `-0.0327` n `6`; index avg `-0.1878` n `23`; metal avg `-0.159` n `18`; unknown avg `2.0879` n `384`
- 24h: commodity avg `-2.3609` n `12`; crypto_alt avg `2.8221` n `228`; crypto_major avg `2.4776` n `8`; equity avg `1.3435` n `66`; fx avg `-0.0355` n `6`; index avg `0.8586` n `23`; metal avg `1.2305` n `18`; unknown avg `3.5163` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
