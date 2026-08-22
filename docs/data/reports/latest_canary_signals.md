# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T08:52:28.148568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.524` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.4564` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.4475` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-4.0594` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.1542` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0189` n `12`; crypto_alt avg `0.4766` n `230`; crypto_major avg `0.5124` n `8`; equity avg `0.0485` n `121`; fx avg `0.0028` n `6`; index avg `0.0033` n `25`; metal avg `0.0141` n `20`; unknown avg `0.1333` n `794`
- 1h: commodity avg `-0.0295` n `12`; crypto_alt avg `-0.7958` n `230`; crypto_major avg `-1.1637` n `8`; equity avg `-0.1132` n `121`; fx avg `0.0094` n `6`; index avg `-0.0095` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0713` n `794`
- 4h: commodity avg `0.0141` n `12`; crypto_alt avg `-5.656` n `230`; crypto_major avg `-4.5099` n `8`; equity avg `-0.4505` n `121`; fx avg `-0.0065` n `6`; index avg `-0.0535` n `25`; metal avg `-0.0624` n `20`; unknown avg `-0.1304` n `778`
- 24h: commodity avg `0.1401` n `12`; crypto_alt avg `2.3922` n `230`; crypto_major avg `2.4037` n `8`; equity avg `-0.8724` n `121`; fx avg `0.0623` n `6`; index avg `-0.1139` n `25`; metal avg `-0.199` n `20`; unknown avg `1.3909` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
