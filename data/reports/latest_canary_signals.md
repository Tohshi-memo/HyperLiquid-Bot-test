# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T04:37:33.204887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.5657` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.4894` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.395` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.0235` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.3317` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0084` n `13`; crypto_alt avg `0.5467` n `239`; crypto_major avg `0.3262` n `8`; equity avg `0.121` n `166`; fx avg `-0.0011` n `6`; index avg `0.0376` n `27`; metal avg `0.0231` n `20`; unknown avg `159.742` n `1258`
- 1h: commodity avg `-0.0148` n `13`; crypto_alt avg `-0.8298` n `239`; crypto_major avg `-1.3288` n `8`; equity avg `-0.3755` n `166`; fx avg `0.0004` n `6`; index avg `0.0029` n `27`; metal avg `-0.0085` n `20`; unknown avg `-0.3014` n `1242`
- 4h: commodity avg `-0.0445` n `13`; crypto_alt avg `-3.6432` n `239`; crypto_major avg `-4.6102` n `8`; equity avg `-1.5867` n `166`; fx avg `-0.0173` n `6`; index avg `-0.1208` n `27`; metal avg `-0.2152` n `20`; unknown avg `1.4905` n `1240`
- 24h: commodity avg `0.2495` n `13`; crypto_alt avg `-6.4006` n `239`; crypto_major avg `-8.4604` n `8`; equity avg `-6.0525` n `166`; fx avg `-0.0603` n `6`; index avg `-0.605` n `27`; metal avg `-0.0876` n `20`; unknown avg `74.4206` n `1109`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
