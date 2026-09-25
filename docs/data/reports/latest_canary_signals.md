# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T11:22:32.251947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2874` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.6881` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6806` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0798` n `12`; crypto_alt avg `0.1155` n `234`; crypto_major avg `0.07` n `8`; equity avg `0.0551` n `141`; fx avg `-0.0099` n `6`; index avg `0.0287` n `26`; metal avg `-0.0528` n `20`; unknown avg `-0.0199` n `944`
- 1h: commodity avg `-0.1095` n `12`; crypto_alt avg `1.0356` n `234`; crypto_major avg `1.2485` n `8`; equity avg `0.0866` n `141`; fx avg `-0.0235` n `6`; index avg `0.023` n `26`; metal avg `0.0022` n `20`; unknown avg `3.5282` n `942`
- 4h: commodity avg `-0.2746` n `12`; crypto_alt avg `2.2735` n `234`; crypto_major avg `2.0128` n `8`; equity avg `0.3322` n `141`; fx avg `-0.0431` n `6`; index avg `0.068` n `26`; metal avg `0.3247` n `20`; unknown avg `2.5184` n `924`
- 24h: commodity avg `-0.0786` n `12`; crypto_alt avg `5.4764` n `234`; crypto_major avg `3.6619` n `8`; equity avg `1.8059` n `141`; fx avg `-0.2482` n `6`; index avg `0.3011` n `26`; metal avg `0.2591` n `20`; unknown avg `12.6459` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
