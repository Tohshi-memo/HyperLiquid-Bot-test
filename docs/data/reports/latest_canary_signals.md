# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T16:37:27.094971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `5.259` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `4.6454` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.2704` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.0953` n `230`; crypto_major avg `0.1674` n `8`; equity avg `-0.0821` n `121`; fx avg `-0.0089` n `6`; index avg `-0.0415` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.0084` n `792`
- 1h: commodity avg `0.0197` n `12`; crypto_alt avg `-0.2762` n `230`; crypto_major avg `0.4454` n `8`; equity avg `0.2942` n `121`; fx avg `-0.0064` n `6`; index avg `-0.021` n `25`; metal avg `0.1236` n `20`; unknown avg `0.1293` n `792`
- 4h: commodity avg `0.2212` n `12`; crypto_alt avg `2.5526` n `230`; crypto_major avg `4.8666` n `8`; equity avg `-0.3924` n `120`; fx avg `0.1133` n `6`; index avg `-0.0891` n `25`; metal avg `0.5962` n `20`; unknown avg `1.2762` n `792`
- 24h: commodity avg `0.3337` n `12`; crypto_alt avg `2.783` n `230`; crypto_major avg `5.2037` n `8`; equity avg `-0.1796` n `120`; fx avg `-0.1867` n `6`; index avg `0.0153` n `25`; metal avg `0.8055` n `20`; unknown avg `0.5296` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
