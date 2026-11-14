# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T18:07:31.315562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1504` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1451` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0537` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5674` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0131` n `13`; crypto_alt avg `-0.3211` n `239`; crypto_major avg `-0.1327` n `8`; equity avg `-0.0409` n `162`; fx avg `-0.0032` n `6`; index avg `-0.007` n `27`; metal avg `0.0016` n `20`; unknown avg `0.1885` n `1256`
- 1h: commodity avg `0.0419` n `13`; crypto_alt avg `0.3651` n `239`; crypto_major avg `0.7974` n `8`; equity avg `0.1665` n `162`; fx avg `-0.0002` n `6`; index avg `0.0107` n `27`; metal avg `0.0423` n `20`; unknown avg `1.5154` n `1260`
- 4h: commodity avg `-0.0635` n `13`; crypto_alt avg `-2.6131` n `239`; crypto_major avg `-2.2139` n `8`; equity avg `-0.6465` n `162`; fx avg `0.0082` n `6`; index avg `-0.0688` n `27`; metal avg `-0.1602` n `20`; unknown avg `0.7694` n `1250`
- 24h: commodity avg `-0.0474` n `13`; crypto_alt avg `-6.5043` n `239`; crypto_major avg `-6.0845` n `8`; equity avg `-1.3266` n `162`; fx avg `-0.0539` n `6`; index avg `-0.0856` n `27`; metal avg `-0.2861` n `20`; unknown avg `2.0642` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
