# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T01:37:20.871263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.0553` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8965` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7844` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0249` n `12`; crypto_alt avg `-0.0861` n `228`; crypto_major avg `0.0671` n `8`; equity avg `0.165` n `74`; fx avg `-0.0084` n `6`; index avg `0.1095` n `23`; metal avg `0.1281` n `18`; unknown avg `0.0857` n `517`
- 1h: commodity avg `-0.0374` n `12`; crypto_alt avg `0.4389` n `228`; crypto_major avg `0.2193` n `8`; equity avg `0.3647` n `74`; fx avg `0.0002` n `6`; index avg `0.2626` n `23`; metal avg `0.4411` n `18`; unknown avg `0.0967` n `517`
- 4h: commodity avg `-0.2506` n `12`; crypto_alt avg `-2.6223` n `228`; crypto_major avg `-2.041` n `8`; equity avg `-0.2566` n `74`; fx avg `0.0282` n `6`; index avg `0.0143` n `23`; metal avg `-0.1445` n `18`; unknown avg `-0.2921` n `517`
- 24h: commodity avg `-1.0283` n `12`; crypto_alt avg `0.0213` n `228`; crypto_major avg `0.484` n `8`; equity avg `1.8425` n `74`; fx avg `-0.2766` n `6`; index avg `0.8403` n `23`; metal avg `0.3926` n `18`; unknown avg `-2.9052` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
