# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T11:37:33.417811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0659` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8387` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.4458` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `-0.1082` n `234`; crypto_major avg `-0.0423` n `8`; equity avg `-0.0711` n `140`; fx avg `0.0015` n `6`; index avg `-0.0066` n `26`; metal avg `0.0567` n `20`; unknown avg `7.5538` n `944`
- 1h: commodity avg `0.0894` n `12`; crypto_alt avg `0.5555` n `234`; crypto_major avg `0.5458` n `8`; equity avg `-0.1627` n `140`; fx avg `0.0254` n `6`; index avg `-0.0081` n `26`; metal avg `0.0972` n `20`; unknown avg `14.145` n `940`
- 4h: commodity avg `-0.1195` n `12`; crypto_alt avg `2.5395` n `234`; crypto_major avg `2.9464` n `8`; equity avg `0.5006` n `140`; fx avg `-0.0255` n `6`; index avg `0.08` n `26`; metal avg `0.1077` n `20`; unknown avg `11.7759` n `934`
- 24h: commodity avg `-0.7712` n `12`; crypto_alt avg `7.1415` n `234`; crypto_major avg `5.9606` n `8`; equity avg `1.913` n `140`; fx avg `-0.0973` n `6`; index avg `0.3638` n `26`; metal avg `0.1031` n `20`; unknown avg `11.4049` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
