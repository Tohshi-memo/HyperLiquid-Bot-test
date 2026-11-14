# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T03:52:25.428340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3568` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.249` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.1716` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.0212` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.3008` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0222` n `13`; crypto_alt avg `0.0028` n `239`; crypto_major avg `-0.1186` n `8`; equity avg `-0.0811` n `162`; fx avg `-0.0046` n `6`; index avg `-0.0061` n `27`; metal avg `-0.0289` n `20`; unknown avg `38.3958` n `1260`
- 1h: commodity avg `-0.0555` n `13`; crypto_alt avg `-0.5034` n `239`; crypto_major avg `-1.3191` n `8`; equity avg `-0.157` n `162`; fx avg `-0.0123` n `6`; index avg `-0.0183` n `27`; metal avg `-0.0302` n `20`; unknown avg `-0.0145` n `1254`
- 4h: commodity avg `0.0385` n `13`; crypto_alt avg `-1.4744` n `239`; crypto_major avg `-2.3183` n `8`; equity avg `-0.2971` n `162`; fx avg `-0.0159` n `6`; index avg `-0.1467` n `27`; metal avg `-0.0693` n `20`; unknown avg `6.542` n `1248`
- 24h: commodity avg `-0.1253` n `13`; crypto_alt avg `-0.1222` n `239`; crypto_major avg `-2.2356` n `8`; equity avg `-2.9193` n `162`; fx avg `-0.0947` n `6`; index avg `-0.2366` n `27`; metal avg `-0.6613` n `20`; unknown avg `59.6045` n `1032`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
