# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T19:37:47.821946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1828` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.7691` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.547` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `0.1016` n `230`; crypto_major avg `-0.0999` n `8`; equity avg `0.1787` n `121`; fx avg `-0.0042` n `6`; index avg `-0.0111` n `25`; metal avg `0.0011` n `20`; unknown avg `0.228` n `792`
- 1h: commodity avg `-0.1312` n `12`; crypto_alt avg `0.5743` n `230`; crypto_major avg `1.6142` n `8`; equity avg `0.388` n `121`; fx avg `-0.0027` n `6`; index avg `-0.0086` n `25`; metal avg `0.1761` n `20`; unknown avg `0.5109` n `792`
- 4h: commodity avg `-0.411` n `12`; crypto_alt avg `0.062` n `230`; crypto_major avg `1.7718` n `8`; equity avg `0.0027` n `121`; fx avg `-0.0265` n `6`; index avg `-0.0675` n `25`; metal avg `0.2248` n `20`; unknown avg `0.2976` n `792`
- 24h: commodity avg `-0.0583` n `12`; crypto_alt avg `3.3372` n `230`; crypto_major avg `6.4458` n `8`; equity avg `-0.2828` n `120`; fx avg `-0.2069` n `6`; index avg `-0.0224` n `25`; metal avg `0.9907` n `20`; unknown avg `0.738` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
