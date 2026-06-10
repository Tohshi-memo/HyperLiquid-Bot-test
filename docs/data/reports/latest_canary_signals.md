# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T00:07:27.987941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1159` n `12`; crypto_alt avg `0.2316` n `228`; crypto_major avg `0.2123` n `8`; equity avg `0.671` n `74`; fx avg `-0.0671` n `6`; index avg `0.2383` n `23`; metal avg `0.2158` n `18`; unknown avg `0.1642` n `547`
- 1h: commodity avg `-0.0777` n `12`; crypto_alt avg `0.3982` n `228`; crypto_major avg `0.2923` n `8`; equity avg `0.5668` n `74`; fx avg `-0.0791` n `6`; index avg `0.1207` n `23`; metal avg `-0.2714` n `18`; unknown avg `0.0271` n `547`
- 4h: commodity avg `0.133` n `12`; crypto_alt avg `-0.2615` n `228`; crypto_major avg `-0.4007` n `8`; equity avg `0.0242` n `74`; fx avg `-0.0586` n `6`; index avg `0.2471` n `23`; metal avg `-0.475` n `18`; unknown avg `-0.258` n `547`
- 24h: commodity avg `-0.6429` n `12`; crypto_alt avg `-0.6279` n `228`; crypto_major avg `-2.5065` n `8`; equity avg `-1.394` n `74`; fx avg `-0.0285` n `6`; index avg `-0.564` n `23`; metal avg `-1.6882` n `18`; unknown avg `-0.3539` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0377`, n `668`, weak_sample_signal
