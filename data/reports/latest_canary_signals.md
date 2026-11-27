# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T05:37:26.516749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0164` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0804` n `13`; crypto_alt avg `0.0624` n `239`; crypto_major avg `-0.0333` n `8`; equity avg `0.0795` n `168`; fx avg `-0.0083` n `6`; index avg `0.0137` n `27`; metal avg `0.0615` n `20`; unknown avg `77.1374` n `1261`
- 1h: commodity avg `0.0468` n `13`; crypto_alt avg `0.1282` n `239`; crypto_major avg `0.2548` n `8`; equity avg `0.7209` n `168`; fx avg `0.0136` n `6`; index avg `0.027` n `27`; metal avg `0.2056` n `20`; unknown avg `6.8867` n `1259`
- 4h: commodity avg `0.1827` n `13`; crypto_alt avg `1.2916` n `239`; crypto_major avg `2.1991` n `8`; equity avg `2.6099` n `168`; fx avg `-0.0006` n `6`; index avg `0.212` n `27`; metal avg `0.9741` n `20`; unknown avg `66.5538` n `1249`
- 24h: commodity avg `0.2671` n `13`; crypto_alt avg `1.8979` n `239`; crypto_major avg `1.9653` n `8`; equity avg `3.1805` n `168`; fx avg `0.021` n `6`; index avg `0.2601` n `27`; metal avg `0.732` n `20`; unknown avg `207.0041` n `991`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
