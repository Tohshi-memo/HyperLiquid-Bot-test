# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T20:07:27.798291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.257` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.5296` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4661` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `-0.2656` n `239`; crypto_major avg `-0.0467` n `8`; equity avg `-0.4477` n `166`; fx avg `-0.0069` n `6`; index avg `-0.0389` n `27`; metal avg `-0.0538` n `20`; unknown avg `19.2459` n `1244`
- 1h: commodity avg `0.109` n `13`; crypto_alt avg `-0.7329` n `239`; crypto_major avg `-0.5508` n `8`; equity avg `-1.5986` n `166`; fx avg `-0.0181` n `6`; index avg `-0.1894` n `27`; metal avg `-0.186` n `20`; unknown avg `177.3096` n `1244`
- 4h: commodity avg `0.4283` n `13`; crypto_alt avg `-0.8626` n `239`; crypto_major avg `-1.8287` n `8`; equity avg `-2.7056` n `166`; fx avg `-0.0192` n `6`; index avg `-0.3626` n `27`; metal avg `-0.2991` n `20`; unknown avg `163.1073` n `1243`
- 24h: commodity avg `0.1725` n `13`; crypto_alt avg `-6.398` n `239`; crypto_major avg `-7.0706` n `8`; equity avg `-8.6762` n `166`; fx avg `-0.0061` n `6`; index avg `-0.8329` n `27`; metal avg `-1.3175` n `20`; unknown avg `39.252` n `1147`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
