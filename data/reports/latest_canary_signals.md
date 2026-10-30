# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T07:52:27.089568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0693` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0723` n `13`; crypto_alt avg `0.0426` n `238`; crypto_major avg `-0.1339` n `8`; equity avg `-0.1252` n `156`; fx avg `0.0028` n `6`; index avg `-0.0301` n `27`; metal avg `-0.0783` n `20`; unknown avg `0.0855` n `1258`
- 1h: commodity avg `0.2713` n `13`; crypto_alt avg `-0.5368` n `238`; crypto_major avg `-1.0649` n `8`; equity avg `-0.3763` n `156`; fx avg `0.0258` n `6`; index avg `0.0044` n `27`; metal avg `-0.1519` n `20`; unknown avg `128.4558` n `1252`
- 4h: commodity avg `0.2327` n `13`; crypto_alt avg `0.7021` n `238`; crypto_major avg `-0.4815` n `8`; equity avg `-0.3906` n `156`; fx avg `-0.0131` n `6`; index avg `0.0542` n `27`; metal avg `-0.2618` n `20`; unknown avg `1.3178` n `1224`
- 24h: commodity avg `0.0821` n `13`; crypto_alt avg `-2.9964` n `238`; crypto_major avg `-0.4204` n `8`; equity avg `-2.8064` n `155`; fx avg `0.1012` n `6`; index avg `-0.2759` n `27`; metal avg `-0.7568` n `20`; unknown avg `30.3962` n `978`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
