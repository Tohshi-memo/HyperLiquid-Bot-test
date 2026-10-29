# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T15:07:29.658316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1623` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7957` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0416` n `13`; crypto_alt avg `0.1547` n `238`; crypto_major avg `0.1881` n `8`; equity avg `0.2295` n `156`; fx avg `0.0114` n `6`; index avg `0.0496` n `27`; metal avg `-0.0351` n `20`; unknown avg `0.2956` n `1232`
- 1h: commodity avg `-0.2493` n `13`; crypto_alt avg `0.7112` n `238`; crypto_major avg `0.7412` n `8`; equity avg `0.0303` n `156`; fx avg `0.0807` n `6`; index avg `0.0126` n `27`; metal avg `0.0677` n `20`; unknown avg `-0.0507` n `1180`
- 4h: commodity avg `-0.492` n `13`; crypto_alt avg `1.4054` n `238`; crypto_major avg `1.6703` n `8`; equity avg `0.4287` n `156`; fx avg `0.0627` n `6`; index avg `-0.0569` n `27`; metal avg `-0.1254` n `20`; unknown avg `0.8226` n `1132`
- 24h: commodity avg `-0.9679` n `13`; crypto_alt avg `0.491` n `238`; crypto_major avg `2.0727` n `8`; equity avg `-0.4344` n `155`; fx avg `0.0184` n `6`; index avg `-0.0989` n `27`; metal avg `-0.4685` n `20`; unknown avg `11.7757` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
