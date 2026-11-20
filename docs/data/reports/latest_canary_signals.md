# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T18:37:36.458427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.6789` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.1584` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.11` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0237` n `13`; crypto_alt avg `-0.0315` n `239`; crypto_major avg `-0.1156` n `8`; equity avg `0.1172` n `166`; fx avg `-0.0069` n `6`; index avg `0.0125` n `27`; metal avg `-0.0364` n `20`; unknown avg `373.959` n `1262`
- 1h: commodity avg `0.0296` n `13`; crypto_alt avg `0.861` n `239`; crypto_major avg `0.5589` n `8`; equity avg `0.3574` n `166`; fx avg `-0.0079` n `6`; index avg `0.0182` n `27`; metal avg `-0.0066` n `20`; unknown avg `0.3314` n `1260`
- 4h: commodity avg `0.1302` n `13`; crypto_alt avg `-2.6522` n `239`; crypto_major avg `-3.5487` n `8`; equity avg `-3.3633` n `166`; fx avg `0.0138` n `6`; index avg `-0.3903` n `27`; metal avg `-0.4387` n `20`; unknown avg `-0.5237` n `1245`
- 24h: commodity avg `-0.2897` n `13`; crypto_alt avg `-6.0926` n `239`; crypto_major avg `-7.1754` n `8`; equity avg `-8.2332` n `166`; fx avg `0.0043` n `6`; index avg `-0.7831` n `27`; metal avg `-1.3694` n `20`; unknown avg `37.1962` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
