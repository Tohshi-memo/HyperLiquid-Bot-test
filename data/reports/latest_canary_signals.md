# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T07:22:25.504151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1169` n `12`; crypto_alt avg `0.0906` n `229`; crypto_major avg `0.1143` n `8`; equity avg `-0.0814` n `91`; fx avg `-0.0117` n `6`; index avg `-0.0108` n `25`; metal avg `0.0273` n `20`; unknown avg `0.0081` n `765`
- 1h: commodity avg `-0.1237` n `12`; crypto_alt avg `-0.0057` n `229`; crypto_major avg `0.0155` n `8`; equity avg `-0.1443` n `91`; fx avg `0.0281` n `6`; index avg `0.0024` n `25`; metal avg `-0.0269` n `20`; unknown avg `0.9756` n `765`
- 4h: commodity avg `-0.2194` n `12`; crypto_alt avg `-0.1002` n `229`; crypto_major avg `0.1201` n `8`; equity avg `-0.8448` n `91`; fx avg `-0.0769` n `6`; index avg `-0.1586` n `25`; metal avg `-0.058` n `20`; unknown avg `-0.0781` n `733`
- 24h: commodity avg `-1.0592` n `12`; crypto_alt avg `0.7011` n `229`; crypto_major avg `0.9254` n `8`; equity avg `0.3114` n `91`; fx avg `-0.1218` n `6`; index avg `0.1756` n `25`; metal avg `0.3255` n `20`; unknown avg `-0.0173` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
