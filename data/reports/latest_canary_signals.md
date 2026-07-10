# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T15:07:26.565669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0715` n `12`; crypto_alt avg `0.2036` n `229`; crypto_major avg `0.0229` n `8`; equity avg `-0.0984` n `91`; fx avg `0.0009` n `6`; index avg `-0.0307` n `25`; metal avg `-0.0484` n `20`; unknown avg `0.0223` n `766`
- 1h: commodity avg `0.0291` n `12`; crypto_alt avg `-0.3608` n `229`; crypto_major avg `-0.4627` n `8`; equity avg `-0.3399` n `91`; fx avg `0.0265` n `6`; index avg `-0.0397` n `25`; metal avg `-0.0606` n `20`; unknown avg `-0.0316` n `766`
- 4h: commodity avg `-0.3678` n `12`; crypto_alt avg `-0.5475` n `229`; crypto_major avg `-0.8422` n `8`; equity avg `-1.0532` n `91`; fx avg `-0.0581` n `6`; index avg `-0.045` n `25`; metal avg `0.0472` n `20`; unknown avg `-0.1512` n `766`
- 24h: commodity avg `-0.6029` n `12`; crypto_alt avg `0.6529` n `229`; crypto_major avg `0.6661` n `8`; equity avg `-1.1519` n `91`; fx avg `-0.1311` n `6`; index avg `-0.0156` n `25`; metal avg `-0.2511` n `20`; unknown avg `-0.2283` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
