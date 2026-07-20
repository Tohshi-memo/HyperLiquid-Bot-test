# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T09:52:30.932260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0371` n `12`; crypto_alt avg `0.1014` n `230`; crypto_major avg `0.0736` n `8`; equity avg `0.2447` n `98`; fx avg `0.002` n `6`; index avg `0.0531` n `25`; metal avg `0.059` n `20`; unknown avg `-0.0145` n `770`
- 1h: commodity avg `-0.045` n `12`; crypto_alt avg `0.3967` n `230`; crypto_major avg `0.3215` n `8`; equity avg `0.467` n `98`; fx avg `-0.0227` n `6`; index avg `0.1129` n `25`; metal avg `0.07` n `20`; unknown avg `0.037` n `770`
- 4h: commodity avg `-0.561` n `12`; crypto_alt avg `1.0556` n `230`; crypto_major avg `0.5044` n `8`; equity avg `0.6883` n `98`; fx avg `-0.0014` n `6`; index avg `0.1764` n `25`; metal avg `0.2944` n `20`; unknown avg `0.0556` n `747`
- 24h: commodity avg `-0.6449` n `12`; crypto_alt avg `0.3427` n `230`; crypto_major avg `-0.1735` n `8`; equity avg `0.535` n `97`; fx avg `-0.0282` n `6`; index avg `0.1344` n `25`; metal avg `0.2549` n `20`; unknown avg `0.0098` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0911`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.083`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0762`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
