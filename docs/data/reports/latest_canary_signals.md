# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T03:37:34.410054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.5381` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.1708` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.0985` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.3192` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `0.246` n `239`; crypto_major avg `0.2239` n `8`; equity avg `-0.1467` n `162`; fx avg `0.0014` n `6`; index avg `-0.0309` n `27`; metal avg `0.0028` n `20`; unknown avg `-0.0468` n `1260`
- 1h: commodity avg `-0.1169` n `13`; crypto_alt avg `-1.2971` n `239`; crypto_major avg `-1.4498` n `8`; equity avg `-0.9608` n `162`; fx avg `-0.009` n `6`; index avg `-0.1306` n `27`; metal avg `0.0047` n `20`; unknown avg `1.8759` n `1254`
- 4h: commodity avg `-0.1585` n `13`; crypto_alt avg `-1.87` n `239`; crypto_major avg `-2.257` n `8`; equity avg `-1.0615` n `162`; fx avg `-0.0151` n `6`; index avg `-0.0862` n `27`; metal avg `0.2811` n `20`; unknown avg `3.6382` n `1247`
- 24h: commodity avg `0.8126` n `13`; crypto_alt avg `-2.4912` n `239`; crypto_major avg `-3.7237` n `8`; equity avg `-1.2345` n `162`; fx avg `-0.0267` n `6`; index avg `0.0017` n `27`; metal avg `-0.3752` n `20`; unknown avg `50.9532` n `1119`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
