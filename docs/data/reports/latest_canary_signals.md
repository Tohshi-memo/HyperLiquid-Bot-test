# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T11:07:32.087693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1453` n `12`; crypto_alt avg `0.2643` n `228`; crypto_major avg `0.3015` n `8`; equity avg `0.1468` n `79`; fx avg `-0.0315` n `6`; index avg `0.0421` n `23`; metal avg `0.0861` n `20`; unknown avg `0.061` n `722`
- 1h: commodity avg `-0.1324` n `12`; crypto_alt avg `0.2567` n `228`; crypto_major avg `0.1457` n `8`; equity avg `0.1124` n `79`; fx avg `-0.0067` n `6`; index avg `0.0355` n `23`; metal avg `0.0435` n `18`; unknown avg `0.3708` n `701`
- 4h: commodity avg `-0.1111` n `12`; crypto_alt avg `0.5729` n `228`; crypto_major avg `0.6265` n `8`; equity avg `0.276` n `79`; fx avg `0.0109` n `6`; index avg `0.0912` n `23`; metal avg `0.0568` n `18`; unknown avg `0.3479` n `693`
- 24h: commodity avg `-0.2565` n `12`; crypto_alt avg `0.0802` n `228`; crypto_major avg `0.2779` n `8`; equity avg `0.0283` n `79`; fx avg `0.0328` n `6`; index avg `0.1009` n `23`; metal avg `0.6257` n `18`; unknown avg `0.552` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
