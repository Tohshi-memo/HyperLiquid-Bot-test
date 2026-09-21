# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T10:52:31.147826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5447` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3663` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5553` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0361` n `12`; crypto_alt avg `0.2348` n `234`; crypto_major avg `-0.0119` n `8`; equity avg `-0.0187` n `140`; fx avg `0.0122` n `6`; index avg `0.001` n `26`; metal avg `-0.014` n `20`; unknown avg `1.1122` n `944`
- 1h: commodity avg `-0.1955` n `12`; crypto_alt avg `0.5429` n `234`; crypto_major avg `0.0206` n `8`; equity avg `0.0159` n `140`; fx avg `0.0101` n `6`; index avg `0.0152` n `26`; metal avg `-0.0083` n `20`; unknown avg `0.1608` n `940`
- 4h: commodity avg `-0.2042` n `12`; crypto_alt avg `1.9361` n `234`; crypto_major avg `2.3405` n `8`; equity avg `0.7852` n `140`; fx avg `-0.0286` n `6`; index avg `0.1038` n `26`; metal avg `-0.0258` n `20`; unknown avg `2.1721` n `934`
- 24h: commodity avg `-0.8227` n `12`; crypto_alt avg `7.0481` n `234`; crypto_major avg `5.4961` n `8`; equity avg `2.0684` n `140`; fx avg `-0.0961` n `6`; index avg `0.374` n `26`; metal avg `-0.0191` n `20`; unknown avg `9.3274` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
