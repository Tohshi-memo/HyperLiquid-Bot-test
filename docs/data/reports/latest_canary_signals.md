# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T06:07:37.352876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.5682` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.4822` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.4089` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.1802` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0261` n `13`; crypto_alt avg `-0.2561` n `239`; crypto_major avg `-0.2096` n `8`; equity avg `-0.1142` n `166`; fx avg `0.0059` n `6`; index avg `-0.0095` n `27`; metal avg `-0.014` n `20`; unknown avg `164.4893` n `1232`
- 1h: commodity avg `0.0193` n `13`; crypto_alt avg `-0.3281` n `239`; crypto_major avg `-0.3636` n `8`; equity avg `-0.0083` n `166`; fx avg `0.0047` n `6`; index avg `0.0072` n `27`; metal avg `-0.0164` n `20`; unknown avg `162.2295` n `1232`
- 4h: commodity avg `-0.0094` n `13`; crypto_alt avg `-3.7943` n `239`; crypto_major avg `-4.5776` n `8`; equity avg `-1.3974` n `166`; fx avg `-0.0248` n `6`; index avg `-0.0954` n `27`; metal avg `-0.1687` n `20`; unknown avg `0.5767` n `1216`
- 24h: commodity avg `0.4421` n `13`; crypto_alt avg `-7.5743` n `239`; crypto_major avg `-9.4892` n `8`; equity avg `-5.7593` n `166`; fx avg `-0.0617` n `6`; index avg `-0.583` n `27`; metal avg `-0.3962` n `20`; unknown avg `20.9284` n `1107`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
