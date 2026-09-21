# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T10:22:33.841617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2621` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0958` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0827` n `12`; crypto_alt avg `0.3196` n `234`; crypto_major avg `0.1217` n `8`; equity avg `0.0195` n `140`; fx avg `-0.0055` n `6`; index avg `0.0002` n `26`; metal avg `0.0133` n `20`; unknown avg `-0.0076` n `944`
- 1h: commodity avg `-0.1775` n `12`; crypto_alt avg `0.1506` n `234`; crypto_major avg `0.2548` n `8`; equity avg `0.0635` n `140`; fx avg `-0.0074` n `6`; index avg `0.0085` n `26`; metal avg `-0.0274` n `20`; unknown avg `1.3078` n `940`
- 4h: commodity avg `-0.1079` n `12`; crypto_alt avg `1.6952` n `234`; crypto_major avg `2.1542` n `8`; equity avg `0.8369` n `140`; fx avg `-0.0596` n `6`; index avg `0.114` n `26`; metal avg `0.0584` n `20`; unknown avg `1.8007` n `912`
- 24h: commodity avg `-0.7225` n `12`; crypto_alt avg `6.7282` n `234`; crypto_major avg `5.5664` n `8`; equity avg `2.0771` n `140`; fx avg `-0.0982` n `6`; index avg `0.3585` n `26`; metal avg `0.0301` n `20`; unknown avg `7.9914` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
