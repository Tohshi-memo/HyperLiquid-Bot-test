# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T05:07:36.996028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.57` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_index_leads_crypto: score `1.4494` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0077` n `13`; crypto_alt avg `-0.0742` n `239`; crypto_major avg `-0.165` n `8`; equity avg `-0.0539` n `166`; fx avg `0.0026` n `6`; index avg `-0.0087` n `27`; metal avg `-0.0204` n `20`; unknown avg `159.3105` n `1255`
- 1h: commodity avg `0.0055` n `13`; crypto_alt avg `-0.1214` n `239`; crypto_major avg `-0.3549` n `8`; equity avg `-0.1355` n `166`; fx avg `-0.0087` n `6`; index avg `-0.0171` n `27`; metal avg `-0.016` n `20`; unknown avg `326.1706` n `1255`
- 4h: commodity avg `-0.0912` n `13`; crypto_alt avg `-0.9959` n `239`; crypto_major avg `-1.5435` n `8`; equity avg `-0.6221` n `166`; fx avg `0.0144` n `6`; index avg `-0.0941` n `27`; metal avg `-0.1401` n `20`; unknown avg `8.2178` n `1253`
- 24h: commodity avg `-0.0071` n `13`; crypto_alt avg `3.0933` n `239`; crypto_major avg `4.8367` n `8`; equity avg `1.4761` n `166`; fx avg `-0.0215` n `6`; index avg `0.1808` n `27`; metal avg `0.1454` n `20`; unknown avg `606.1837` n `1076`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
