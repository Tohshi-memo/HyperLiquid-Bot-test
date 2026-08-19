# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T17:13:35.695092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `5.2446` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.7303` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.4868` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `-0.2375` n `230`; crypto_major avg `-0.3605` n `8`; equity avg `-0.2983` n `121`; fx avg `0.0069` n `6`; index avg `-0.0173` n `25`; metal avg `-0.0537` n `20`; unknown avg `0.1346` n `792`
- 1h: commodity avg `0.0416` n `12`; crypto_alt avg `0.0312` n `230`; crypto_major avg `-0.5098` n `8`; equity avg `-0.4988` n `121`; fx avg `-0.0106` n `6`; index avg `-0.075` n `25`; metal avg `-0.0445` n `20`; unknown avg `-0.1358` n `792`
- 4h: commodity avg `0.1982` n `12`; crypto_alt avg `2.3657` n `230`; crypto_major avg `3.9285` n `8`; equity avg `-1.3161` n `120`; fx avg `0.0509` n `6`; index avg `-0.1746` n `25`; metal avg `0.4417` n `20`; unknown avg `1.1685` n `792`
- 24h: commodity avg `0.412` n `12`; crypto_alt avg `2.7007` n `230`; crypto_major avg `4.6577` n `8`; equity avg `-0.6154` n `120`; fx avg `-0.1822` n `6`; index avg `-0.0305` n `25`; metal avg `0.7714` n `20`; unknown avg `0.4879` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
