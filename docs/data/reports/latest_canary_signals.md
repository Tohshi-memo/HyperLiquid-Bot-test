# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T13:07:19.404692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1516` n `12`; crypto_alt avg `-0.3761` n `228`; crypto_major avg `-0.2981` n `8`; equity avg `0.0016` n `69`; fx avg `-0.0013` n `6`; index avg `0.0197` n `23`; metal avg `-0.1963` n `18`; unknown avg `0.7093` n `422`
- 1h: commodity avg `-0.8186` n `12`; crypto_alt avg `-0.1634` n `228`; crypto_major avg `-0.1056` n `8`; equity avg `-0.0006` n `69`; fx avg `0.0058` n `6`; index avg `-0.0073` n `23`; metal avg `-0.1363` n `18`; unknown avg `0.7222` n `422`
- 4h: commodity avg `-1.2754` n `12`; crypto_alt avg `-0.541` n `228`; crypto_major avg `-0.1347` n `8`; equity avg `-0.3093` n `69`; fx avg `-0.0079` n `6`; index avg `-0.0991` n `23`; metal avg `0.1298` n `18`; unknown avg `2.0359` n `416`
- 24h: commodity avg `-0.1785` n `12`; crypto_alt avg `-1.0885` n `228`; crypto_major avg `-0.9587` n `8`; equity avg `-0.4093` n `69`; fx avg `0.0015` n `6`; index avg `0.5182` n `23`; metal avg `0.1966` n `18`; unknown avg `4.2495` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2893`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
