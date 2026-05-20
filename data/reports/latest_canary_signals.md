# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T23:52:17.768875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0893` n `12`; crypto_alt avg `-0.0015` n `228`; crypto_major avg `0.0723` n `8`; equity avg `0.0332` n `66`; fx avg `0.0313` n `6`; index avg `0.0427` n `23`; metal avg `0.0928` n `18`; unknown avg `1.7902` n `384`
- 1h: commodity avg `-0.1392` n `12`; crypto_alt avg `0.0808` n `228`; crypto_major avg `0.2508` n `8`; equity avg `0.0399` n `66`; fx avg `0.0231` n `6`; index avg `0.02` n `23`; metal avg `0.1859` n `18`; unknown avg `2.1551` n `384`
- 4h: commodity avg `-0.048` n `12`; crypto_alt avg `-0.3258` n `228`; crypto_major avg `0.2103` n `8`; equity avg `-0.2414` n `66`; fx avg `-0.0325` n `6`; index avg `-0.2009` n `23`; metal avg `-0.159` n `18`; unknown avg `1.8019` n `384`
- 24h: commodity avg `-2.472` n `12`; crypto_alt avg `2.8132` n `228`; crypto_major avg `2.3549` n `8`; equity avg `1.3126` n `66`; fx avg `-0.0352` n `6`; index avg `0.8451` n `23`; metal avg `1.2306` n `18`; unknown avg `3.1947` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0438`, n `668`, weak_sample_signal
