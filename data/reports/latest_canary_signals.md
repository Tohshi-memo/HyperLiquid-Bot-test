# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T14:37:28.955357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.6556` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6539` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0273` n `13`; crypto_alt avg `0.0051` n `238`; crypto_major avg `-0.0544` n `8`; equity avg `-0.1456` n `155`; fx avg `0.0153` n `6`; index avg `-0.016` n `27`; metal avg `-0.0007` n `20`; unknown avg `-0.0357` n `1238`
- 1h: commodity avg `0.0314` n `13`; crypto_alt avg `-0.7187` n `238`; crypto_major avg `-0.6669` n `8`; equity avg `-0.1417` n `155`; fx avg `0.0262` n `6`; index avg `-0.0383` n `27`; metal avg `-0.0999` n `20`; unknown avg `0.4876` n `1154`
- 4h: commodity avg `0.2429` n `13`; crypto_alt avg `-1.5833` n `238`; crypto_major avg `-1.6665` n `8`; equity avg `-0.9107` n `155`; fx avg `0.0915` n `6`; index avg `-0.0109` n `27`; metal avg `-0.0126` n `20`; unknown avg `0.9362` n `1150`
- 24h: commodity avg `0.5573` n `13`; crypto_alt avg `0.0604` n `238`; crypto_major avg `0.1838` n `8`; equity avg `1.5461` n `154`; fx avg `0.1765` n `6`; index avg `0.3464` n `27`; metal avg `-0.0944` n `20`; unknown avg `7.4842` n `1066`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
