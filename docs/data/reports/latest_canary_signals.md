# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T22:37:28.940154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.0245` n `230`; crypto_major avg `-0.1015` n `8`; equity avg `-0.0151` n `98`; fx avg `-0.0022` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0034` n `20`; unknown avg `0.0741` n `770`
- 1h: commodity avg `0.0402` n `12`; crypto_alt avg `-0.4209` n `230`; crypto_major avg `-0.4631` n `8`; equity avg `-0.12` n `98`; fx avg `-0.0188` n `6`; index avg `-0.0319` n `25`; metal avg `-0.0622` n `20`; unknown avg `0.1582` n `770`
- 4h: commodity avg `-0.0745` n `12`; crypto_alt avg `-0.3555` n `230`; crypto_major avg `-0.5126` n `8`; equity avg `-0.7277` n `98`; fx avg `-0.044` n `6`; index avg `-0.1388` n `25`; metal avg `-0.0795` n `20`; unknown avg `0.1005` n `770`
- 24h: commodity avg `-0.4039` n `12`; crypto_alt avg `1.2562` n `230`; crypto_major avg `0.8705` n `8`; equity avg `-0.4475` n `98`; fx avg `-0.1989` n `6`; index avg `-0.049` n `25`; metal avg `0.1888` n `20`; unknown avg `0.1686` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1079`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0878`, n `666`, weak_sample_signal
