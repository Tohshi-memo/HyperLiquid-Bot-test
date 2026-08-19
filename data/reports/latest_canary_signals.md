# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T16:52:31.501199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `5.2488` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.9946` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.6832` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0359` n `12`; crypto_alt avg `0.0464` n `230`; crypto_major avg `-0.099` n `8`; equity avg `-0.1278` n `121`; fx avg `-0.0082` n `6`; index avg `-0.0101` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.1055` n `792`
- 1h: commodity avg `0.0955` n `12`; crypto_alt avg `0.4714` n `230`; crypto_major avg `0.2888` n `8`; equity avg `0.2033` n `121`; fx avg `-0.0088` n `6`; index avg `-0.0069` n `25`; metal avg `0.065` n `20`; unknown avg `-0.0983` n `792`
- 4h: commodity avg `0.224` n `12`; crypto_alt avg `2.5014` n `230`; crypto_major avg `4.2186` n `8`; equity avg `-1.0302` n `120`; fx avg `0.0546` n `6`; index avg `-0.1638` n `25`; metal avg `0.5354` n `20`; unknown avg `1.1815` n `792`
- 24h: commodity avg `0.4355` n `12`; crypto_alt avg `2.9458` n `230`; crypto_major avg `4.8571` n `8`; equity avg `-0.4964` n `120`; fx avg `-0.1973` n `6`; index avg `-0.0349` n `25`; metal avg `0.8107` n `20`; unknown avg `0.5028` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
