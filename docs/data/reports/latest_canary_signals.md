# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T17:36:36.514000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0201` n `12`; crypto_alt avg `-0.0537` n `230`; crypto_major avg `-0.0675` n `8`; equity avg `-0.0715` n `114`; fx avg `0.0061` n `6`; index avg `-0.0088` n `25`; metal avg `-0.0163` n `20`; unknown avg `-0.069` n `791`
- 1h: commodity avg `0.0896` n `12`; crypto_alt avg `-0.0167` n `230`; crypto_major avg `-0.0546` n `8`; equity avg `0.0001` n `114`; fx avg `-0.0229` n `6`; index avg `-0.0082` n `25`; metal avg `-0.0265` n `20`; unknown avg `-0.1661` n `791`
- 4h: commodity avg `0.3277` n `12`; crypto_alt avg `0.6998` n `230`; crypto_major avg `0.3839` n `8`; equity avg `-0.1896` n `114`; fx avg `0.0894` n `6`; index avg `-0.0863` n `25`; metal avg `0.0011` n `20`; unknown avg `0.016` n `786`
- 24h: commodity avg `0.1477` n `12`; crypto_alt avg `0.5962` n `230`; crypto_major avg `-0.4352` n `8`; equity avg `-0.6597` n `114`; fx avg `0.0731` n `6`; index avg `-0.1349` n `25`; metal avg `0.14` n `20`; unknown avg `0.0956` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
