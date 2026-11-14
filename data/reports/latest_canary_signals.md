# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T21:37:35.611326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.6925` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.6294` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.2964` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.9463` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.8908` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.6794` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.6275` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0208` n `13`; crypto_alt avg `0.242` n `239`; crypto_major avg `0.0114` n `8`; equity avg `0.1544` n `162`; fx avg `-0.0027` n `6`; index avg `0.0084` n `27`; metal avg `-0.0175` n `20`; unknown avg `-0.1434` n `1262`
- 1h: commodity avg `-0.0145` n `13`; crypto_alt avg `-1.5449` n `239`; crypto_major avg `-1.9054` n `8`; equity avg `-0.2779` n `162`; fx avg `0.0007` n `6`; index avg `-0.0146` n `27`; metal avg `-0.226` n `20`; unknown avg `39.9266` n `1240`
- 4h: commodity avg `0.0169` n `13`; crypto_alt avg `-4.2025` n `239`; crypto_major avg `-3.6756` n `8`; equity avg `-0.7293` n `162`; fx avg `0.0051` n `6`; index avg `-0.0462` n `27`; metal avg `-0.3792` n `20`; unknown avg `0.1337` n `1214`
- 24h: commodity avg `-0.1557` n `13`; crypto_alt avg `-9.2321` n `239`; crypto_major avg `-8.5436` n `8`; equity avg `-1.8207` n `162`; fx avg `-0.0045` n `6`; index avg `-0.1277` n `27`; metal avg `-0.4858` n `20`; unknown avg `-0.0178` n `1098`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
