# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T15:22:29.462131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0178` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.9427` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.216` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `-0.117` n `239`; crypto_major avg `-0.3685` n `8`; equity avg `-0.1312` n `166`; fx avg `0.0094` n `6`; index avg `-0.014` n `27`; metal avg `-0.0147` n `20`; unknown avg `0.3881` n `1260`
- 1h: commodity avg `-0.0092` n `13`; crypto_alt avg `0.2524` n `239`; crypto_major avg `-0.2694` n `8`; equity avg `-0.0716` n `166`; fx avg `0.0136` n `6`; index avg `-0.0316` n `27`; metal avg `0.002` n `20`; unknown avg `313.6633` n `1260`
- 4h: commodity avg `0.0721` n `13`; crypto_alt avg `2.9001` n `239`; crypto_major avg `3.0899` n `8`; equity avg `0.8739` n `166`; fx avg `0.0234` n `6`; index avg `0.0899` n `27`; metal avg `0.1472` n `20`; unknown avg `205.9548` n `1226`
- 24h: commodity avg `0.7507` n `13`; crypto_alt avg `0.6284` n `239`; crypto_major avg `0.4157` n `8`; equity avg `-2.319` n `166`; fx avg `-0.0851` n `6`; index avg `-0.3164` n `27`; metal avg `0.0308` n `20`; unknown avg `22.5152` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
