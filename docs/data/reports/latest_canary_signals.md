# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T03:37:31.000329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1167` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0205` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.02` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8773` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.4393` n `239`; crypto_major avg `-0.8078` n `8`; equity avg `-0.0608` n `162`; fx avg `0.0081` n `6`; index avg `-0.0064` n `27`; metal avg `-0.0052` n `20`; unknown avg `166.0584` n `1260`
- 1h: commodity avg `-0.005` n `13`; crypto_alt avg `-0.1151` n `239`; crypto_major avg `-0.7226` n `8`; equity avg `-0.002` n `162`; fx avg `-0.0002` n `6`; index avg `-0.0095` n `27`; metal avg `0.0159` n `20`; unknown avg `-0.5045` n `1258`
- 4h: commodity avg `0.0581` n `13`; crypto_alt avg `-1.3236` n `239`; crypto_major avg `-2.0586` n `8`; equity avg `-0.1813` n `162`; fx avg `-0.0239` n `6`; index avg `-0.0381` n `27`; metal avg `-0.0386` n `20`; unknown avg `2.1796` n `1248`
- 24h: commodity avg `-0.1079` n `13`; crypto_alt avg `-1.026` n `239`; crypto_major avg `-2.8958` n `8`; equity avg `-3.0761` n `162`; fx avg `-0.0881` n `6`; index avg `-0.2579` n `27`; metal avg `-0.6544` n `20`; unknown avg `59.3183` n `1034`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
