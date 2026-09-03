# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T14:52:37.410370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2732` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5655` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.5547` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.7814` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.501` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0786` n `12`; crypto_alt avg `0.6414` n `232`; crypto_major avg `0.6292` n `8`; equity avg `0.0583` n `133`; fx avg `0.0086` n `6`; index avg `0.0169` n `26`; metal avg `0.1053` n `20`; unknown avg `-0.2357` n `792`
- 1h: commodity avg `-0.0806` n `12`; crypto_alt avg `1.1908` n `232`; crypto_major avg `1.7029` n `8`; equity avg `-0.0785` n `133`; fx avg `0.0211` n `6`; index avg `-0.0652` n `26`; metal avg `0.2019` n `20`; unknown avg `1.0148` n `790`
- 4h: commodity avg `-0.2699` n `12`; crypto_alt avg `1.5567` n `232`; crypto_major avg `3.0033` n `8`; equity avg `0.4486` n `133`; fx avg `-0.0391` n `6`; index avg `0.118` n `26`; metal avg `0.4378` n `20`; unknown avg `23.2545` n `790`
- 24h: commodity avg `0.2094` n `12`; crypto_alt avg `3.2223` n `232`; crypto_major avg `4.0241` n `8`; equity avg `1.0465` n `133`; fx avg `-0.3012` n `6`; index avg `0.0191` n `26`; metal avg `0.6522` n `20`; unknown avg `0.1616` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0428`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0415`, n `668`, weak_sample_signal
