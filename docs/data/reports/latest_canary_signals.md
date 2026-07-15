# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T13:07:26.400469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0764` n `12`; crypto_alt avg `0.4028` n `230`; crypto_major avg `0.5521` n `8`; equity avg `-0.0062` n `93`; fx avg `0.0075` n `6`; index avg `0.0063` n `25`; metal avg `0.1401` n `20`; unknown avg `0.0727` n `768`
- 1h: commodity avg `-0.0692` n `12`; crypto_alt avg `1.1252` n `230`; crypto_major avg `1.315` n `8`; equity avg `0.3201` n `93`; fx avg `0.0127` n `6`; index avg `0.0737` n `25`; metal avg `0.3485` n `20`; unknown avg `0.3701` n `767`
- 4h: commodity avg `-0.0243` n `12`; crypto_alt avg `1.2591` n `230`; crypto_major avg `1.3442` n `8`; equity avg `0.0706` n `93`; fx avg `0.0179` n `6`; index avg `0.0039` n `25`; metal avg `0.1929` n `20`; unknown avg `0.1179` n `767`
- 24h: commodity avg `-0.1189` n `12`; crypto_alt avg `1.7587` n `230`; crypto_major avg `2.8115` n `8`; equity avg `0.6744` n `92`; fx avg `0.0489` n `6`; index avg `0.1978` n `25`; metal avg `0.1738` n `20`; unknown avg `0.3297` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
