# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T07:22:30.209068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6711` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0131` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5757` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0716` n `12`; crypto_alt avg `0.1821` n `228`; crypto_major avg `0.0833` n `8`; equity avg `0.1438` n `86`; fx avg `0.0148` n `6`; index avg `0.0078` n `23`; metal avg `0.022` n `20`; unknown avg `0.0395` n `765`
- 1h: commodity avg `-0.1455` n `12`; crypto_alt avg `0.9565` n `228`; crypto_major avg `0.8895` n `8`; equity avg `0.4971` n `86`; fx avg `0.0446` n `6`; index avg `0.0798` n `23`; metal avg `0.2428` n `20`; unknown avg `0.2127` n `757`
- 4h: commodity avg `0.0183` n `12`; crypto_alt avg `2.3778` n `228`; crypto_major avg `2.6894` n `8`; equity avg `1.1137` n `86`; fx avg `-0.0674` n `6`; index avg `0.2003` n `23`; metal avg `0.6763` n `20`; unknown avg `0.4746` n `717`
- 24h: commodity avg `0.1663` n `12`; crypto_alt avg `-1.4549` n `228`; crypto_major avg `-1.5922` n `8`; equity avg `-3.6938` n `86`; fx avg `0.0243` n `6`; index avg `-0.5538` n `23`; metal avg `0.6617` n `20`; unknown avg `0.634` n `693`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
