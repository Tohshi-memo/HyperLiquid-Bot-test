# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T15:52:31.383261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6094` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1695` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0954` n `13`; crypto_alt avg `0.2609` n `238`; crypto_major avg `0.1634` n `8`; equity avg `-0.1202` n `156`; fx avg `0.043` n `6`; index avg `-0.0167` n `27`; metal avg `-0.0009` n `20`; unknown avg `0.14` n `1238`
- 1h: commodity avg `0.1704` n `13`; crypto_alt avg `1.1411` n `238`; crypto_major avg `0.9951` n `8`; equity avg `0.5448` n `156`; fx avg `0.0489` n `6`; index avg `0.0669` n `27`; metal avg `-0.0308` n `20`; unknown avg `0.7388` n `1232`
- 4h: commodity avg `-0.4037` n `13`; crypto_alt avg `2.3134` n `238`; crypto_major avg `2.2057` n `8`; equity avg `0.9089` n `156`; fx avg `0.0935` n `6`; index avg `0.0114` n `27`; metal avg `0.0362` n `20`; unknown avg `1.1302` n `1132`
- 24h: commodity avg `-0.9024` n `13`; crypto_alt avg `1.4579` n `238`; crypto_major avg `3.044` n `8`; equity avg `-0.2029` n `155`; fx avg `0.0527` n `6`; index avg `-0.0914` n `27`; metal avg `-0.435` n `20`; unknown avg `15.2661` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
