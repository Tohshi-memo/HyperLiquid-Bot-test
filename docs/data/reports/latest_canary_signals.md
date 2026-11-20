# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T18:07:28.144817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.9169` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.5816` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.5808` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0391` n `13`; crypto_alt avg `0.2036` n `239`; crypto_major avg `0.206` n `8`; equity avg `-0.0231` n `166`; fx avg `0.0046` n `6`; index avg `-0.0022` n `27`; metal avg `0.0126` n `20`; unknown avg `0.716` n `1252`
- 1h: commodity avg `-0.0011` n `13`; crypto_alt avg `0.4582` n `239`; crypto_major avg `0.0287` n `8`; equity avg `0.2113` n `166`; fx avg `-0.0162` n `6`; index avg `-0.0378` n `27`; metal avg `-0.06` n `20`; unknown avg `0.6228` n `1257`
- 4h: commodity avg `-0.0752` n `13`; crypto_alt avg `-3.3077` n `239`; crypto_major avg `-3.9921` n `8`; equity avg `-3.7934` n `166`; fx avg `0.0116` n `6`; index avg `-0.4105` n `27`; metal avg `-0.4113` n `20`; unknown avg `-0.7759` n `1245`
- 24h: commodity avg `-0.3775` n `13`; crypto_alt avg `-5.6767` n `239`; crypto_major avg `-6.5689` n `8`; equity avg `-7.9069` n `166`; fx avg `0.018` n `6`; index avg `-0.7291` n `27`; metal avg `-1.2662` n `20`; unknown avg `36.9745` n `1151`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
