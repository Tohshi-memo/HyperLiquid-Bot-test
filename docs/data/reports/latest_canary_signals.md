# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T17:07:15.725618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0251` n `12`; crypto_alt avg `0.4037` n `228`; crypto_major avg `0.273` n `8`; equity avg `0.0614` n `65`; fx avg `0.0` n `5`; index avg `0.0355` n `23`; metal avg `0.0175` n `18`; unknown avg `0.071` n `376`
- 1h: commodity avg `0.0483` n `12`; crypto_alt avg `0.6058` n `228`; crypto_major avg `0.2899` n `8`; equity avg `0.0928` n `65`; fx avg `0.0` n `5`; index avg `0.0175` n `23`; metal avg `0.0441` n `18`; unknown avg `0.0619` n `376`
- 4h: commodity avg `0.3487` n `12`; crypto_alt avg `-0.1708` n `228`; crypto_major avg `-0.0349` n `8`; equity avg `0.0828` n `65`; fx avg `-0.0138` n `5`; index avg `0.0268` n `23`; metal avg `-0.0365` n `18`; unknown avg `-0.269` n `376`
- 24h: commodity avg `-0.0992` n `12`; crypto_alt avg `1.3586` n `228`; crypto_major avg `1.4523` n `8`; equity avg `1.7793` n `65`; fx avg `0.0031` n `5`; index avg `0.5434` n `23`; metal avg `0.0334` n `18`; unknown avg `0.389` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
