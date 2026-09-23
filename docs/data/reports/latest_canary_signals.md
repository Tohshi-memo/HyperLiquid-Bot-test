# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T16:22:31.198367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6065` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3279` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2366` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9482` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `0.1212` n `234`; crypto_major avg `-0.1476` n `8`; equity avg `-0.061` n `141`; fx avg `-0.0002` n `6`; index avg `-0.0054` n `26`; metal avg `0.0166` n `20`; unknown avg `-0.0294` n `943`
- 1h: commodity avg `0.0992` n `12`; crypto_alt avg `-1.0546` n `234`; crypto_major avg `-0.8544` n `8`; equity avg `-0.3794` n `141`; fx avg `0.0018` n `6`; index avg `-0.0692` n `26`; metal avg `-0.0854` n `20`; unknown avg `-0.4551` n `927`
- 4h: commodity avg `0.1111` n `12`; crypto_alt avg `-3.7322` n `234`; crypto_major avg `-2.4954` n `8`; equity avg `-0.5472` n `141`; fx avg `-0.013` n `6`; index avg `-0.1675` n `26`; metal avg `-0.2588` n `20`; unknown avg `514.3078` n `891`
- 24h: commodity avg `0.3913` n `12`; crypto_alt avg `-1.3942` n `234`; crypto_major avg `-2.457` n `8`; equity avg `-0.759` n `140`; fx avg `0.007` n `6`; index avg `-0.2511` n `26`; metal avg `-0.4848` n `20`; unknown avg `15.1845` n `838`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2512`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
