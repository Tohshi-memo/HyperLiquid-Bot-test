# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T15:23:06.415678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5682` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2597` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5867` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0493` n `13`; crypto_alt avg `0.4786` n `238`; crypto_major avg `0.5342` n `8`; equity avg `0.2506` n `156`; fx avg `0.0215` n `6`; index avg `0.0166` n `27`; metal avg `-0.0152` n `20`; unknown avg `19.964` n `1238`
- 1h: commodity avg `-0.212` n `13`; crypto_alt avg `1.2743` n `238`; crypto_major avg `1.2098` n `8`; equity avg `0.1469` n `156`; fx avg `0.06` n `6`; index avg `0.0156` n `27`; metal avg `-0.01` n `20`; unknown avg `1.1054` n `1180`
- 4h: commodity avg `-0.4412` n `13`; crypto_alt avg `1.7982` n `238`; crypto_major avg `2.127` n `8`; equity avg `0.5403` n `156`; fx avg `0.0726` n `6`; index avg `-0.0455` n `27`; metal avg `-0.1327` n `20`; unknown avg `1.8925` n `1132`
- 24h: commodity avg `-0.8404` n `13`; crypto_alt avg `0.8288` n `238`; crypto_major avg `2.5496` n `8`; equity avg `-0.3027` n `155`; fx avg `0.0456` n `6`; index avg `-0.1008` n `27`; metal avg `-0.4863` n `20`; unknown avg `14.9486` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
