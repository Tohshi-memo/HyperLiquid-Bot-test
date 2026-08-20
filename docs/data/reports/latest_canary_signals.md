# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T09:52:27.437226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.6186` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.3167` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.0137` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0428` n `12`; crypto_alt avg `-0.3149` n `230`; crypto_major avg `-0.4205` n `8`; equity avg `0.0056` n `121`; fx avg `0.0032` n `6`; index avg `0.0094` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.1581` n `792`
- 1h: commodity avg `0.0632` n `12`; crypto_alt avg `-0.0648` n `230`; crypto_major avg `-0.1035` n `8`; equity avg `0.2037` n `121`; fx avg `0.0003` n `6`; index avg `0.0414` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.1296` n `792`
- 4h: commodity avg `0.3206` n `12`; crypto_alt avg `1.8271` n `230`; crypto_major avg `2.3343` n `8`; equity avg `-0.2843` n `121`; fx avg `0.0551` n `6`; index avg `-0.0485` n `25`; metal avg `0.0176` n `20`; unknown avg `0.5692` n `776`
- 24h: commodity avg `0.238` n `12`; crypto_alt avg `7.2568` n `230`; crypto_major avg `12.2426` n `8`; equity avg `0.4346` n `120`; fx avg `0.2271` n `6`; index avg `0.0919` n `25`; metal avg `0.9252` n `20`; unknown avg `2.3313` n `775`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
