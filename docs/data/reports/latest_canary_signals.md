# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T11:53:03.236896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.5403` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.7212` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.3518` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.0042` n `230`; crypto_major avg `-0.0368` n `8`; equity avg `-0.2528` n `121`; fx avg `0.0044` n `6`; index avg `-0.0522` n `25`; metal avg `-0.1141` n `20`; unknown avg `0.0034` n `792`
- 1h: commodity avg `0.1046` n `12`; crypto_alt avg `0.4035` n `230`; crypto_major avg `0.6147` n `8`; equity avg `-0.6897` n `121`; fx avg `0.0115` n `6`; index avg `-0.1593` n `25`; metal avg `-0.1683` n `20`; unknown avg `0.3342` n `792`
- 4h: commodity avg `0.2883` n `12`; crypto_alt avg `2.2096` n `230`; crypto_major avg `2.6401` n `8`; equity avg `-0.9002` n `121`; fx avg `0.0704` n `6`; index avg `-0.1835` n `25`; metal avg `-0.0811` n `20`; unknown avg `0.6633` n `792`
- 24h: commodity avg `0.2614` n `12`; crypto_alt avg `7.9982` n `230`; crypto_major avg `13.0208` n `8`; equity avg `0.1322` n `120`; fx avg `0.2265` n `6`; index avg `0.0049` n `25`; metal avg `0.7777` n `20`; unknown avg `2.8776` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
