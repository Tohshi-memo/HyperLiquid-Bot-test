# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T23:52:24.091951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.0282` n `230`; crypto_major avg `-0.0062` n `8`; equity avg `0.003` n `96`; fx avg `-0.0006` n `6`; index avg `-0.0003` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.0742` n `770`
- 1h: commodity avg `-0.0323` n `12`; crypto_alt avg `-0.0399` n `230`; crypto_major avg `-0.0746` n `8`; equity avg `0.0235` n `96`; fx avg `-0.0061` n `6`; index avg `0.0091` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.2619` n `770`
- 4h: commodity avg `0.0162` n `12`; crypto_alt avg `0.2619` n `230`; crypto_major avg `0.2177` n `8`; equity avg `0.0309` n `96`; fx avg `0.0065` n `6`; index avg `0.0049` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.3147` n `770`
- 24h: commodity avg `0.2913` n `12`; crypto_alt avg `-0.281` n `230`; crypto_major avg `0.5998` n `8`; equity avg `-0.187` n `96`; fx avg `-0.0785` n `6`; index avg `0.0613` n `25`; metal avg `-0.0314` n `20`; unknown avg `0.071` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
