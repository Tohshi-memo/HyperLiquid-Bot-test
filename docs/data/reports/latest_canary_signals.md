# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T10:15:59.081127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.8138` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.6655` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.3137` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0149` n `12`; crypto_alt avg `0.225` n `230`; crypto_major avg `0.3014` n `8`; equity avg `0.1601` n `121`; fx avg `0.0143` n `6`; index avg `0.0365` n `25`; metal avg `0.038` n `20`; unknown avg `-0.0355` n `792`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `0.137` n `230`; crypto_major avg `-0.0493` n `8`; equity avg `0.1424` n `121`; fx avg `0.0256` n `6`; index avg `0.0448` n `25`; metal avg `0.0359` n `20`; unknown avg `0.0749` n `792`
- 4h: commodity avg `0.3218` n `12`; crypto_alt avg `2.022` n `230`; crypto_major avg `2.6355` n `8`; equity avg `-0.1783` n `121`; fx avg `0.0988` n `6`; index avg `-0.0421` n `25`; metal avg `-0.03` n `20`; unknown avg `0.4381` n `792`
- 24h: commodity avg `0.2223` n `12`; crypto_alt avg `7.7929` n `230`; crypto_major avg `12.9052` n `8`; equity avg `0.8711` n `120`; fx avg `0.2305` n `6`; index avg `0.1574` n `25`; metal avg `0.9274` n `20`; unknown avg `2.4841` n `775`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
