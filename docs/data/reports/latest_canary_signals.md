# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T12:37:26.011430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0467` n `12`; crypto_alt avg `-0.0372` n `230`; crypto_major avg `0.0138` n `8`; equity avg `0.2212` n `98`; fx avg `0.0029` n `6`; index avg `0.0568` n `25`; metal avg `-0.0179` n `20`; unknown avg `0.0759` n `773`
- 1h: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.2026` n `230`; crypto_major avg `-0.2657` n `8`; equity avg `-0.2184` n `98`; fx avg `0.0062` n `6`; index avg `-0.0235` n `25`; metal avg `0.0631` n `20`; unknown avg `-0.1003` n `773`
- 4h: commodity avg `0.0462` n `12`; crypto_alt avg `0.0651` n `230`; crypto_major avg `-0.0773` n `8`; equity avg `-0.3256` n `98`; fx avg `-0.006` n `6`; index avg `-0.0416` n `25`; metal avg `0.0817` n `20`; unknown avg `0.4564` n `773`
- 24h: commodity avg `0.5449` n `12`; crypto_alt avg `-0.8543` n `230`; crypto_major avg `-1.6522` n `8`; equity avg `0.2587` n `98`; fx avg `-0.0049` n `6`; index avg `-0.0558` n `25`; metal avg `0.4683` n `20`; unknown avg `0.5981` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.104`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0912`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0797`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
