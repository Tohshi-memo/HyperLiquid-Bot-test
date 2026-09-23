# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T16:37:36.857183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7372` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.459` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.4167` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.0008` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `0.0203` n `234`; crypto_major avg `-0.0369` n `8`; equity avg `0.0849` n `141`; fx avg `-0.0106` n `6`; index avg `0.0067` n `26`; metal avg `0.035` n `20`; unknown avg `0.355` n `943`
- 1h: commodity avg `-0.0681` n `12`; crypto_alt avg `-0.0995` n `234`; crypto_major avg `-0.2234` n `8`; equity avg `-0.1536` n `141`; fx avg `-0.0231` n `6`; index avg `-0.0217` n `26`; metal avg `0.0558` n `20`; unknown avg `-0.0858` n `927`
- 4h: commodity avg `0.1403` n `12`; crypto_alt avg `-3.8744` n `234`; crypto_major avg `-2.5969` n `8`; equity avg `-0.5961` n `141`; fx avg `-0.0424` n `6`; index avg `-0.1802` n `26`; metal avg `-0.1379` n `20`; unknown avg `512.6848` n `891`
- 24h: commodity avg `0.4271` n `12`; crypto_alt avg `-1.5738` n `234`; crypto_major avg `-2.5895` n `8`; equity avg `-0.7426` n `140`; fx avg `-0.0042` n `6`; index avg `-0.2448` n `26`; metal avg `-0.4812` n `20`; unknown avg `14.5822` n `846`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2542`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
