# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T08:22:41.508892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4844` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3291` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.2698` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0031` n `13`; crypto_alt avg `-0.3051` n `239`; crypto_major avg `-0.3758` n `8`; equity avg `-0.1153` n `166`; fx avg `0.0058` n `6`; index avg `-0.0106` n `27`; metal avg `-0.0194` n `20`; unknown avg `159.1437` n `1260`
- 1h: commodity avg `-0.0189` n `13`; crypto_alt avg `-0.8056` n `239`; crypto_major avg `-1.3008` n `8`; equity avg `-0.3295` n `166`; fx avg `0.0089` n `6`; index avg `-0.031` n `27`; metal avg `-0.0595` n `20`; unknown avg `322.1008` n `1240`
- 4h: commodity avg `-0.0197` n `13`; crypto_alt avg `1.6491` n `239`; crypto_major avg `2.4647` n `8`; equity avg `0.9977` n `166`; fx avg `-0.0868` n `6`; index avg `0.1222` n `27`; metal avg `0.1356` n `20`; unknown avg `43.5937` n `1208`
- 24h: commodity avg `0.5315` n `13`; crypto_alt avg `-6.476` n `239`; crypto_major avg `-7.541` n `8`; equity avg `-5.4644` n `166`; fx avg `-0.1085` n `6`; index avg `-0.6153` n `27`; metal avg `-0.4364` n `20`; unknown avg `21.6423` n `1141`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
