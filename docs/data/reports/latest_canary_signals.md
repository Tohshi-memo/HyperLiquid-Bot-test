# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T04:52:30.692288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0924` n `229`; crypto_major avg `-0.091` n `8`; equity avg `-0.012` n `88`; fx avg `0.0` n `6`; index avg `0.0006` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0029` n `765`
- 1h: commodity avg `-0.0077` n `12`; crypto_alt avg `0.0937` n `229`; crypto_major avg `0.1608` n `8`; equity avg `0.0699` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0148` n `25`; metal avg `0.0112` n `20`; unknown avg `1.5752` n `765`
- 4h: commodity avg `0.0204` n `12`; crypto_alt avg `-0.6982` n `229`; crypto_major avg `-0.5961` n `8`; equity avg `0.1415` n `88`; fx avg `0.0023` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.5635` n `763`
- 24h: commodity avg `0.0737` n `12`; crypto_alt avg `-0.9844` n `229`; crypto_major avg `-1.2895` n `8`; equity avg `0.1436` n `88`; fx avg `-0.0084` n `6`; index avg `0.0128` n `25`; metal avg `0.0775` n `20`; unknown avg `-0.9056` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
