# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T05:22:31.357732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.0255` n `228`; crypto_major avg `-0.0035` n `8`; equity avg `-0.0104` n `88`; fx avg `0.0038` n `6`; index avg `-0.0222` n `25`; metal avg `-0.0216` n `20`; unknown avg `5.9406` n `763`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `0.1181` n `228`; crypto_major avg `0.0149` n `8`; equity avg `0.1577` n `88`; fx avg `0.0139` n `6`; index avg `0.0599` n `25`; metal avg `-0.1087` n `20`; unknown avg `0.7156` n `763`
- 4h: commodity avg `0.0677` n `12`; crypto_alt avg `0.9615` n `228`; crypto_major avg `1.1254` n `8`; equity avg `-0.2906` n `88`; fx avg `-0.0145` n `6`; index avg `-0.0198` n `25`; metal avg `0.0856` n `20`; unknown avg `0.2198` n `759`
- 24h: commodity avg `-0.6413` n `12`; crypto_alt avg `1.6115` n `228`; crypto_major avg `1.1412` n `8`; equity avg `-1.4681` n `88`; fx avg `0.0167` n `6`; index avg `-0.3622` n `25`; metal avg `1.061` n `20`; unknown avg `24.9411` n `735`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
