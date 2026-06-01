# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T13:10:51.315650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1033` n `12`; crypto_alt avg `-0.5189` n `228`; crypto_major avg `-0.371` n `8`; equity avg `-0.0699` n `69`; fx avg `-0.0276` n `6`; index avg `-0.0685` n `23`; metal avg `-0.2727` n `18`; unknown avg `0.6691` n `422`
- 1h: commodity avg `-0.5651` n `12`; crypto_alt avg `-0.3062` n `228`; crypto_major avg `-0.1786` n `8`; equity avg `-0.0723` n `69`; fx avg `-0.0206` n `6`; index avg `-0.0954` n `23`; metal avg `-0.2127` n `18`; unknown avg `0.682` n `422`
- 4h: commodity avg `-1.0231` n `12`; crypto_alt avg `-0.6835` n `228`; crypto_major avg `-0.2076` n `8`; equity avg `-0.3807` n `69`; fx avg `-0.0343` n `6`; index avg `-0.1873` n `23`; metal avg `0.0533` n `18`; unknown avg `2.0178` n `416`
- 24h: commodity avg `0.0792` n `12`; crypto_alt avg `-1.2298` n `228`; crypto_major avg `-1.0306` n `8`; equity avg `-0.4805` n `69`; fx avg `-0.0249` n `6`; index avg `0.4296` n `23`; metal avg `0.1198` n `18`; unknown avg `4.2202` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2893`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
