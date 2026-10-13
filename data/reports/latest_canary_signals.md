# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T00:37:32.455590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.862` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.7195` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.654` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.8269` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0191` n `13`; crypto_alt avg `0.0134` n `235`; crypto_major avg `0.221` n `8`; equity avg `0.1347` n `151`; fx avg `-0.0177` n `6`; index avg `0.0065` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.2377` n `1135`
- 1h: commodity avg `-0.0225` n `13`; crypto_alt avg `-0.8371` n `235`; crypto_major avg `-0.6166` n `8`; equity avg `-0.4119` n `151`; fx avg `-0.0254` n `6`; index avg `-0.1105` n `26`; metal avg `-0.1169` n `20`; unknown avg `2.1804` n `1127`
- 4h: commodity avg `0.065` n `13`; crypto_alt avg `-3.4508` n `235`; crypto_major avg `-2.797` n `8`; equity avg `-0.9701` n `151`; fx avg `-0.019` n `6`; index avg `-0.143` n `26`; metal avg `-0.0775` n `20`; unknown avg `4.2751` n `1080`
- 24h: commodity avg `0.7194` n `13`; crypto_alt avg `-6.212` n `235`; crypto_major avg `-4.3944` n `8`; equity avg `-4.5737` n `151`; fx avg `-0.157` n `6`; index avg `-0.5286` n `26`; metal avg `-0.3201` n `20`; unknown avg `0.5634` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2063`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1838`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1208`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0855`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0825`, n `666`, weak_sample_signal
