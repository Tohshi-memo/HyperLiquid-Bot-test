# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T18:22:25.188694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.0166` n `229`; crypto_major avg `-0.0312` n `8`; equity avg `0.0243` n `88`; fx avg `0.0` n `6`; index avg `0.0071` n `25`; metal avg `-0.0` n `20`; unknown avg `0.103` n `765`
- 1h: commodity avg `-0.0045` n `12`; crypto_alt avg `0.1734` n `229`; crypto_major avg `-0.0005` n `8`; equity avg `0.0732` n `88`; fx avg `-0.0018` n `6`; index avg `0.0099` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.0239` n `765`
- 4h: commodity avg `-0.0011` n `12`; crypto_alt avg `0.3686` n `229`; crypto_major avg `0.1715` n `8`; equity avg `0.124` n `88`; fx avg `-0.0063` n `6`; index avg `0.0245` n `25`; metal avg `-0.0066` n `20`; unknown avg `0.1359` n `695`
- 24h: commodity avg `0.0186` n `12`; crypto_alt avg `-1.5268` n `229`; crypto_major avg `-1.0525` n `8`; equity avg `0.3407` n `88`; fx avg `-0.0722` n `6`; index avg `0.0994` n `25`; metal avg `0.0452` n `20`; unknown avg `0.0074` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
