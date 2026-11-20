# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T19:37:31.147435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.348` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4328` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2564` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0465` n `13`; crypto_alt avg `0.1043` n `239`; crypto_major avg `0.2187` n `8`; equity avg `-0.296` n `166`; fx avg `0.0012` n `6`; index avg `-0.0472` n `27`; metal avg `-0.0265` n `20`; unknown avg `5.5464` n `1262`
- 1h: commodity avg `0.2591` n `13`; crypto_alt avg `-0.8511` n `239`; crypto_major avg `-1.4153` n `8`; equity avg `-1.0286` n `166`; fx avg `-0.015` n `6`; index avg `-0.1589` n `27`; metal avg `-0.0668` n `20`; unknown avg `1.3333` n `1256`
- 4h: commodity avg `0.5587` n `13`; crypto_alt avg `-0.5564` n `239`; crypto_major avg `-1.7893` n `8`; equity avg `-2.1573` n `166`; fx avg `0.0077` n `6`; index avg `-0.3565` n `27`; metal avg `-0.3498` n `20`; unknown avg `0.1342` n `1243`
- 24h: commodity avg `0.107` n `13`; crypto_alt avg `-6.3342` n `239`; crypto_major avg `-7.3894` n `8`; equity avg `-8.7045` n `166`; fx avg `0.0027` n `6`; index avg `-0.8885` n `27`; metal avg `-1.335` n `20`; unknown avg `44.8036` n `1149`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
