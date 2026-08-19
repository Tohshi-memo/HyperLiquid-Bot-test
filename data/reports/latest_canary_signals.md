# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T18:58:06.134166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.716` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.4547` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `3.3142` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0394` n `12`; crypto_alt avg `0.0791` n `230`; crypto_major avg `0.0945` n `8`; equity avg `0.0199` n `121`; fx avg `0.0062` n `6`; index avg `-0.0051` n `25`; metal avg `0.0993` n `20`; unknown avg `0.0226` n `792`
- 1h: commodity avg `-0.2541` n `12`; crypto_alt avg `0.0632` n `230`; crypto_major avg `0.2127` n `8`; equity avg `-0.2198` n `121`; fx avg `-0.0046` n `6`; index avg `0.001` n `25`; metal avg `0.0807` n `20`; unknown avg `0.9895` n `792`
- 4h: commodity avg `-0.2346` n `12`; crypto_alt avg `1.8811` n `230`; crypto_major avg `3.4814` n `8`; equity avg `0.0267` n `121`; fx avg `0.0223` n `6`; index avg `-0.035` n `25`; metal avg `0.1672` n `20`; unknown avg `0.0922` n `792`
- 24h: commodity avg `0.0154` n `12`; crypto_alt avg `2.7892` n `230`; crypto_major avg `4.8872` n `8`; equity avg `-0.552` n `120`; fx avg `-0.1895` n `6`; index avg `-0.0057` n `25`; metal avg `0.901` n `20`; unknown avg `0.4248` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
