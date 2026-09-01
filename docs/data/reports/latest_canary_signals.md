# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T18:52:32.094279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3293` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4662` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0349` n `12`; crypto_alt avg `0.4249` n `232`; crypto_major avg `0.4188` n `8`; equity avg `-0.0328` n `131`; fx avg `-0.0045` n `6`; index avg `-0.0234` n `26`; metal avg `0.0085` n `20`; unknown avg `2.1518` n `793`
- 1h: commodity avg `0.0993` n `12`; crypto_alt avg `-0.4527` n `232`; crypto_major avg `-0.6032` n `8`; equity avg `-0.3376` n `131`; fx avg `-0.006` n `6`; index avg `-0.0858` n `26`; metal avg `-0.1355` n `20`; unknown avg `0.4854` n `791`
- 4h: commodity avg `0.6208` n `12`; crypto_alt avg `-1.4443` n `232`; crypto_major avg `-1.7085` n `8`; equity avg `-0.7596` n `131`; fx avg `-0.0017` n `6`; index avg `-0.2423` n `26`; metal avg `-0.2688` n `20`; unknown avg `-0.9528` n `790`
- 24h: commodity avg `0.8391` n `12`; crypto_alt avg `-0.8097` n `232`; crypto_major avg `-2.482` n `8`; equity avg `-1.7451` n `130`; fx avg `0.03` n `6`; index avg `-0.3151` n `26`; metal avg `-0.779` n `20`; unknown avg `0.2417` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0449`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0392`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0362`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.036`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0312`, n `668`, weak_sample_signal
