# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T00:07:31.433670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9036` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.8499` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.7384` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6678` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0273` n `13`; crypto_alt avg `-0.7727` n `235`; crypto_major avg `-0.6357` n `8`; equity avg `-0.5662` n `151`; fx avg `0.0224` n `6`; index avg `-0.0825` n `26`; metal avg `-0.0812` n `20`; unknown avg `17.7422` n `1127`
- 1h: commodity avg `-0.0819` n `13`; crypto_alt avg `-1.0339` n `235`; crypto_major avg `-1.0462` n `8`; equity avg `-0.8677` n `151`; fx avg `0.0333` n `6`; index avg `-0.1224` n `26`; metal avg `-0.0628` n `20`; unknown avg `8.3812` n `1127`
- 4h: commodity avg `0.004` n `13`; crypto_alt avg `-3.3662` n `235`; crypto_major avg `-2.8996` n `8`; equity avg `-1.2318` n `151`; fx avg `0.0271` n `6`; index avg `-0.1612` n `26`; metal avg `-0.0497` n `20`; unknown avg `9.3106` n `1080`
- 24h: commodity avg `0.6288` n `13`; crypto_alt avg `-6.2856` n `235`; crypto_major avg `-4.4211` n `8`; equity avg `-4.6819` n `151`; fx avg `-0.0979` n `6`; index avg `-0.5047` n `26`; metal avg `-0.2453` n `20`; unknown avg `0.6001` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2053`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.181`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1179`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1016`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0818`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `666`, weak_sample_signal
