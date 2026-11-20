# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T21:07:31.422309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0948` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3561` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.028` n `13`; crypto_alt avg `-0.0529` n `239`; crypto_major avg `-0.197` n `8`; equity avg `0.1966` n `166`; fx avg `0.003` n `6`; index avg `0.064` n `27`; metal avg `-0.0535` n `20`; unknown avg `2.3688` n `1224`
- 1h: commodity avg `0.1744` n `13`; crypto_alt avg `-0.152` n `239`; crypto_major avg `-0.4536` n `8`; equity avg `0.2673` n `166`; fx avg `0.0007` n `6`; index avg `0.0093` n `27`; metal avg `0.0335` n `20`; unknown avg `114.1086` n `1230`
- 4h: commodity avg `0.5328` n `13`; crypto_alt avg `-0.3734` n `239`; crypto_major avg `-1.562` n `8`; equity avg `-0.8942` n `166`; fx avg `-0.0429` n `6`; index avg `-0.2059` n `27`; metal avg `-0.1291` n `20`; unknown avg `3.5033` n `1219`
- 24h: commodity avg `0.3069` n `13`; crypto_alt avg `-6.2715` n `239`; crypto_major avg `-7.2152` n `8`; equity avg `-7.9471` n `166`; fx avg `-0.0097` n `6`; index avg `-0.7731` n `27`; metal avg `-1.1837` n `20`; unknown avg `9.3887` n `1129`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
