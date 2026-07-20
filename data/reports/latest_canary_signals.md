# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T17:22:29.961683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `12`; crypto_alt avg `-0.078` n `230`; crypto_major avg `-0.1972` n `8`; equity avg `0.145` n `98`; fx avg `0.0021` n `6`; index avg `0.0137` n `25`; metal avg `0.001` n `20`; unknown avg `0.0162` n `770`
- 1h: commodity avg `0.0893` n `12`; crypto_alt avg `0.0788` n `230`; crypto_major avg `-0.1332` n `8`; equity avg `-0.2641` n `98`; fx avg `-0.0107` n `6`; index avg `-0.1042` n `25`; metal avg `-0.0583` n `20`; unknown avg `0.1613` n `770`
- 4h: commodity avg `-0.0492` n `12`; crypto_alt avg `0.8514` n `230`; crypto_major avg `0.9449` n `8`; equity avg `-0.2288` n `98`; fx avg `-0.0845` n `6`; index avg `-0.062` n `25`; metal avg `0.0457` n `20`; unknown avg `0.2429` n `770`
- 24h: commodity avg `-0.4943` n `12`; crypto_alt avg `1.7509` n `230`; crypto_major avg `1.2005` n `8`; equity avg `0.6673` n `97`; fx avg `-0.1581` n `6`; index avg `0.21` n `25`; metal avg `0.2004` n `20`; unknown avg `0.345` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0968`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0873`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0828`, n `666`, weak_sample_signal
