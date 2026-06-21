# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T12:22:30.181117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `-0.1569` n `228`; crypto_major avg `-0.243` n `8`; equity avg `-0.0102` n `78`; fx avg `-0.0322` n `6`; index avg `-0.011` n `23`; metal avg `-0.0112` n `18`; unknown avg `0.0839` n `702`
- 1h: commodity avg `0.2073` n `12`; crypto_alt avg `-0.2074` n `228`; crypto_major avg `-0.412` n `8`; equity avg `-0.025` n `78`; fx avg `-0.0205` n `6`; index avg `-0.0151` n `23`; metal avg `-0.0008` n `18`; unknown avg `0.055` n `702`
- 4h: commodity avg `0.1614` n `12`; crypto_alt avg `0.0577` n `228`; crypto_major avg `-0.3832` n `8`; equity avg `-0.0696` n `78`; fx avg `-0.013` n `6`; index avg `0.0021` n `23`; metal avg `-0.0553` n `18`; unknown avg `-0.1662` n `702`
- 24h: commodity avg `0.2962` n `12`; crypto_alt avg `1.0114` n `228`; crypto_major avg `-0.742` n `8`; equity avg `0.2905` n `78`; fx avg `-0.0013` n `6`; index avg `0.0212` n `23`; metal avg `-0.0765` n `18`; unknown avg `0.0227` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
