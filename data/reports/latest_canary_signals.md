# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T18:22:38.238170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.8904` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.6909` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.1803` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0386` n `12`; crypto_alt avg `0.033` n `230`; crypto_major avg `0.1388` n `8`; equity avg `-0.0928` n `121`; fx avg `-0.0073` n `6`; index avg `-0.0138` n `25`; metal avg `-0.0544` n `20`; unknown avg `1.034` n `792`
- 1h: commodity avg `-0.1795` n `12`; crypto_alt avg `0.0418` n `230`; crypto_major avg `0.3813` n `8`; equity avg `-0.215` n `121`; fx avg `-0.0114` n `6`; index avg `-0.0286` n `25`; metal avg `-0.0437` n `20`; unknown avg `1.0866` n `792`
- 4h: commodity avg `-0.05` n `12`; crypto_alt avg `2.2169` n `230`; crypto_major avg `3.8404` n `8`; equity avg `0.6601` n `121`; fx avg `-0.0025` n `6`; index avg `0.0341` n `25`; metal avg `0.1495` n `20`; unknown avg `0.114` n `792`
- 24h: commodity avg `0.1852` n `12`; crypto_alt avg `2.6246` n `230`; crypto_major avg `4.6342` n `8`; equity avg `-0.5897` n `120`; fx avg `-0.2109` n `6`; index avg `-0.0551` n `25`; metal avg `0.7793` n `20`; unknown avg `0.4223` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
