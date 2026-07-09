# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T15:07:39.579942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1042` n `12`; crypto_alt avg `0.0899` n `229`; crypto_major avg `0.3916` n `8`; equity avg `0.3541` n `91`; fx avg `0.0074` n `6`; index avg `0.0538` n `25`; metal avg `0.122` n `20`; unknown avg `0.1689` n `765`
- 1h: commodity avg `-0.2646` n `12`; crypto_alt avg `-0.1521` n `229`; crypto_major avg `0.1885` n `8`; equity avg `-0.1814` n `91`; fx avg `-0.0183` n `6`; index avg `-0.0353` n `25`; metal avg `0.0254` n `20`; unknown avg `-0.0469` n `765`
- 4h: commodity avg `-0.7162` n `12`; crypto_alt avg `0.1943` n `229`; crypto_major avg `0.4318` n `8`; equity avg `1.2165` n `91`; fx avg `-0.0307` n `6`; index avg `0.2868` n `25`; metal avg `0.4899` n `20`; unknown avg `0.1579` n `764`
- 24h: commodity avg `-1.3022` n `12`; crypto_alt avg `1.6972` n `229`; crypto_major avg `1.4472` n `8`; equity avg `3.0704` n `91`; fx avg `0.0557` n `6`; index avg `0.5236` n `25`; metal avg `1.2299` n `20`; unknown avg `1.0114` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
