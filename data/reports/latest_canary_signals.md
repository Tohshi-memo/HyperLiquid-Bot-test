# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T08:07:32.172043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.042` n `12`; crypto_alt avg `0.0316` n `229`; crypto_major avg `0.0982` n `8`; equity avg `-0.1652` n `91`; fx avg `0.0014` n `6`; index avg `-0.0101` n `25`; metal avg `0.0041` n `20`; unknown avg `0.0132` n `765`
- 1h: commodity avg `-0.2004` n `12`; crypto_alt avg `0.1128` n `229`; crypto_major avg `0.1082` n `8`; equity avg `-0.2924` n `91`; fx avg `-0.0025` n `6`; index avg `-0.0387` n `25`; metal avg `-0.0681` n `20`; unknown avg `0.0262` n `765`
- 4h: commodity avg `-0.3335` n `12`; crypto_alt avg `-0.1537` n `229`; crypto_major avg `-0.138` n `8`; equity avg `-1.0698` n `91`; fx avg `-0.0607` n `6`; index avg `-0.1932` n `25`; metal avg `-0.1373` n `20`; unknown avg `0.0054` n `733`
- 24h: commodity avg `-0.8896` n `12`; crypto_alt avg `0.5637` n `229`; crypto_major avg `0.854` n `8`; equity avg `-0.2096` n `91`; fx avg `-0.1479` n `6`; index avg `0.1093` n `25`; metal avg `0.1576` n `20`; unknown avg `-0.0169` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
