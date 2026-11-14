# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T23:52:25.813596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5944` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4991` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2661` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.1718` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0037` n `13`; crypto_alt avg `1.1651` n `239`; crypto_major avg `1.2738` n `8`; equity avg `0.3324` n `162`; fx avg `0.0012` n `6`; index avg `0.028` n `27`; metal avg `0.0406` n `20`; unknown avg `0.8337` n `1262`
- 1h: commodity avg `0.0103` n `13`; crypto_alt avg `1.3762` n `239`; crypto_major avg `1.3848` n `8`; equity avg `0.3047` n `162`; fx avg `-0.0111` n `6`; index avg `0.0258` n `27`; metal avg `0.0445` n `20`; unknown avg `238.4333` n `1258`
- 4h: commodity avg `0.1012` n `13`; crypto_alt avg `-1.7127` n `239`; crypto_major avg `-2.4932` n `8`; equity avg `-0.3214` n `162`; fx avg `0.0131` n `6`; index avg `0.0059` n `27`; metal avg `-0.2271` n `20`; unknown avg `-0.5365` n `1176`
- 24h: commodity avg `0.0417` n `13`; crypto_alt avg `-8.2068` n `239`; crypto_major avg `-7.9189` n `8`; equity avg `-1.3526` n `162`; fx avg `0.0174` n `6`; index avg `-0.211` n `27`; metal avg `-0.4481` n `20`; unknown avg `46.291` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
