# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T18:52:27.329690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0325` n `12`; crypto_alt avg `0.1431` n `229`; crypto_major avg `0.2832` n `8`; equity avg `0.0403` n `88`; fx avg `-0.003` n `6`; index avg `0.0059` n `25`; metal avg `0.009` n `20`; unknown avg `-0.0073` n `765`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `0.3609` n `229`; crypto_major avg `0.4159` n `8`; equity avg `0.0771` n `88`; fx avg `-0.0067` n `6`; index avg `0.0186` n `25`; metal avg `0.0111` n `20`; unknown avg `0.0116` n `765`
- 4h: commodity avg `-0.0261` n `12`; crypto_alt avg `0.4468` n `229`; crypto_major avg `0.4249` n `8`; equity avg `0.1523` n `88`; fx avg `-0.0029` n `6`; index avg `0.0115` n `25`; metal avg `0.0046` n `20`; unknown avg `0.0072` n `695`
- 24h: commodity avg `-0.0064` n `12`; crypto_alt avg `-1.2892` n `229`; crypto_major avg `-0.6879` n `8`; equity avg `0.4` n `88`; fx avg `-0.0778` n `6`; index avg `0.1158` n `25`; metal avg `0.0749` n `20`; unknown avg `-0.015` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
