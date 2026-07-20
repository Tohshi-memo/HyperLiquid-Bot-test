# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T19:07:35.151976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.0961` n `230`; crypto_major avg `-0.0807` n `8`; equity avg `-0.245` n `98`; fx avg `0.0039` n `6`; index avg `-0.032` n `25`; metal avg `-0.0335` n `20`; unknown avg `-0.0884` n `770`
- 1h: commodity avg `0.208` n `12`; crypto_alt avg `-0.1966` n `230`; crypto_major avg `-0.3635` n `8`; equity avg `-0.6992` n `98`; fx avg `0.0017` n `6`; index avg `-0.1221` n `25`; metal avg `-0.0807` n `20`; unknown avg `0.3315` n `770`
- 4h: commodity avg `0.2963` n `12`; crypto_alt avg `0.8106` n `230`; crypto_major avg `0.7869` n `8`; equity avg `-0.0924` n `98`; fx avg `-0.0137` n `6`; index avg `-0.0675` n `25`; metal avg `-0.0512` n `20`; unknown avg `0.0334` n `770`
- 24h: commodity avg `-0.2747` n `12`; crypto_alt avg `1.8317` n `230`; crypto_major avg `1.4239` n `8`; equity avg `0.0303` n `98`; fx avg `-0.1452` n `6`; index avg `0.0786` n `25`; metal avg `0.1005` n `20`; unknown avg `0.2741` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1023`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0887`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0832`, n `666`, weak_sample_signal
