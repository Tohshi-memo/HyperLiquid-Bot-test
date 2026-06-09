# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T17:22:27.740637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5623` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.4812` n `12`; crypto_alt avg `0.8571` n `228`; crypto_major avg `0.4025` n `8`; equity avg `0.8012` n `74`; fx avg `0.0106` n `6`; index avg `0.2524` n `23`; metal avg `0.2325` n `18`; unknown avg `0.3159` n `547`
- 1h: commodity avg `0.2762` n `12`; crypto_alt avg `1.5595` n `228`; crypto_major avg `0.9663` n `8`; equity avg `1.5278` n `74`; fx avg `-0.0406` n `6`; index avg `0.4087` n `23`; metal avg `0.1856` n `18`; unknown avg `0.6381` n `547`
- 4h: commodity avg `-0.604` n `12`; crypto_alt avg `-0.5202` n `228`; crypto_major avg `-1.1326` n `8`; equity avg `-3.6949` n `74`; fx avg `-0.0566` n `6`; index avg `-2.5444` n `23`; metal avg `-2.1148` n `18`; unknown avg `1.434` n `545`
- 24h: commodity avg `-1.2125` n `12`; crypto_alt avg `-1.8956` n `228`; crypto_major avg `-2.5874` n `8`; equity avg `-2.9658` n `74`; fx avg `0.0934` n `6`; index avg `-1.9837` n `23`; metal avg `-1.544` n `18`; unknown avg `-1.3986` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
