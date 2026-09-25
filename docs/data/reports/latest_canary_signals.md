# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T11:37:24.659206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4815` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9356` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8453` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0423` n `12`; crypto_alt avg `0.1048` n `234`; crypto_major avg `-0.0961` n `8`; equity avg `-0.0434` n `141`; fx avg `0.0212` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0563` n `20`; unknown avg `2.495` n `944`
- 1h: commodity avg `-0.1355` n `12`; crypto_alt avg `0.8679` n `234`; crypto_major avg `0.724` n `8`; equity avg `0.0543` n `141`; fx avg `0.0059` n `6`; index avg `0.0398` n `26`; metal avg `-0.0383` n `20`; unknown avg `1.9622` n `942`
- 4h: commodity avg `-0.2841` n `12`; crypto_alt avg `2.6311` n `234`; crypto_major avg `2.1974` n `8`; equity avg `0.3521` n `141`; fx avg `-0.0364` n `6`; index avg `0.0793` n `26`; metal avg `0.2618` n `20`; unknown avg `5.2427` n `924`
- 24h: commodity avg `-0.1155` n `12`; crypto_alt avg `5.9083` n `234`; crypto_major avg `3.8107` n `8`; equity avg `1.8459` n `141`; fx avg `-0.2275` n `6`; index avg `0.3207` n `26`; metal avg `0.2369` n `20`; unknown avg `14.576` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
