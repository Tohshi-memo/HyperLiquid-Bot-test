# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T04:37:30.685223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1105` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.076` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0726` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.8634` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.008` n `13`; crypto_alt avg `0.0965` n `239`; crypto_major avg `0.142` n `8`; equity avg `-0.0068` n `162`; fx avg `0.0005` n `6`; index avg `-0.0007` n `27`; metal avg `0.0156` n `20`; unknown avg `7.7006` n `1262`
- 1h: commodity avg `-0.0255` n `13`; crypto_alt avg `0.0306` n `239`; crypto_major avg `0.154` n `8`; equity avg `-0.0238` n `162`; fx avg `0.0004` n `6`; index avg `-0.0032` n `27`; metal avg `-0.0133` n `20`; unknown avg `42.4746` n `1250`
- 4h: commodity avg `-0.014` n `13`; crypto_alt avg `-1.2972` n `239`; crypto_major avg `-2.1245` n `8`; equity avg `-0.2611` n `162`; fx avg `-0.0106` n `6`; index avg `-0.0519` n `27`; metal avg `-0.0485` n `20`; unknown avg `6.3602` n `1248`
- 24h: commodity avg `-0.1783` n `13`; crypto_alt avg `-0.1759` n `239`; crypto_major avg `-1.7991` n `8`; equity avg `-2.8327` n `162`; fx avg `-0.0949` n `6`; index avg `-0.2543` n `27`; metal avg `-0.5721` n `20`; unknown avg `65.0644` n `1032`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
