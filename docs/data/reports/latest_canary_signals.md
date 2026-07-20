# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T23:37:32.965879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0009` n `230`; crypto_major avg `0.0119` n `8`; equity avg `0.0054` n `98`; fx avg `0.0035` n `6`; index avg `0.0082` n `25`; metal avg `0.0087` n `20`; unknown avg `-0.1615` n `770`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `0.1797` n `230`; crypto_major avg `0.2394` n `8`; equity avg `0.1884` n `98`; fx avg `0.0113` n `6`; index avg `0.0765` n `25`; metal avg `0.0292` n `20`; unknown avg `-0.3013` n `770`
- 4h: commodity avg `0.0067` n `12`; crypto_alt avg `0.274` n `230`; crypto_major avg `0.335` n `8`; equity avg `0.0377` n `98`; fx avg `-0.0212` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0333` n `20`; unknown avg `-0.2661` n `770`
- 24h: commodity avg `-0.3327` n `12`; crypto_alt avg `1.5169` n `230`; crypto_major avg `1.0441` n `8`; equity avg `-0.2553` n `98`; fx avg `-0.1921` n `6`; index avg `-0.0013` n `25`; metal avg `0.2197` n `20`; unknown avg `0.0082` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1068`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.103`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0919`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0856`, n `666`, weak_sample_signal
