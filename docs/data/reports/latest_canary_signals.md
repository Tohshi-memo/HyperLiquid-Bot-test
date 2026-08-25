# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T04:37:33.613511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7234` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `0.0238` n `231`; crypto_major avg `-0.1071` n `8`; equity avg `-0.0177` n `122`; fx avg `-0.0101` n `6`; index avg `-0.0072` n `25`; metal avg `-0.035` n `20`; unknown avg `-0.0833` n `794`
- 1h: commodity avg `-0.0773` n `12`; crypto_alt avg `-0.3459` n `231`; crypto_major avg `-0.5252` n `8`; equity avg `0.1621` n `122`; fx avg `0.0002` n `6`; index avg `0.028` n `25`; metal avg `-0.0874` n `20`; unknown avg `0.6946` n `794`
- 4h: commodity avg `0.0148` n `12`; crypto_alt avg `1.1694` n `231`; crypto_major avg `1.2283` n `8`; equity avg `0.904` n `122`; fx avg `0.0085` n `6`; index avg `0.1554` n `25`; metal avg `-0.4951` n `20`; unknown avg `0.2275` n `794`
- 24h: commodity avg `0.002` n `12`; crypto_alt avg `1.5291` n `231`; crypto_major avg `2.4138` n `8`; equity avg `-0.4279` n `122`; fx avg `0.02` n `6`; index avg `-0.0753` n `25`; metal avg `-0.1809` n `20`; unknown avg `0.5322` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
