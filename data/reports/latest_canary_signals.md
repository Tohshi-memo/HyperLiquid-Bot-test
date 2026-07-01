# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T13:07:38.561806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1669` n `12`; crypto_alt avg `0.2296` n `228`; crypto_major avg `0.378` n `8`; equity avg `-0.1508` n `88`; fx avg `-0.0047` n `6`; index avg `-0.0159` n `23`; metal avg `-0.128` n `20`; unknown avg `0.1029` n `765`
- 1h: commodity avg `0.0452` n `12`; crypto_alt avg `0.0948` n `228`; crypto_major avg `0.3383` n `8`; equity avg `-0.9207` n `88`; fx avg `-0.0228` n `6`; index avg `-0.0805` n `23`; metal avg `-0.0008` n `20`; unknown avg `0.0306` n `765`
- 4h: commodity avg `0.1845` n `12`; crypto_alt avg `-0.2134` n `228`; crypto_major avg `-0.7181` n `8`; equity avg `-0.9468` n `88`; fx avg `-0.009` n `6`; index avg `-0.0666` n `23`; metal avg `0.4222` n `20`; unknown avg `-0.2968` n `765`
- 24h: commodity avg `-0.616` n `12`; crypto_alt avg `1.2195` n `228`; crypto_major avg `0.4601` n `8`; equity avg `0.0776` n `88`; fx avg `0.0947` n `6`; index avg `-0.0781` n `23`; metal avg `-0.2908` n `20`; unknown avg `-0.0504` n `743`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
