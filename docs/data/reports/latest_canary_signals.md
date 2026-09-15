# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T19:22:27.610820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.333` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0442` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `0.0563` n `233`; crypto_major avg `-0.0477` n `8`; equity avg `0.0379` n `137`; fx avg `-0.0069` n `6`; index avg `-0.0069` n `27`; metal avg `-0.038` n `20`; unknown avg `-0.2106` n `918`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.808` n `233`; crypto_major avg `-1.3493` n `8`; equity avg `-0.1502` n `137`; fx avg `-0.0031` n `6`; index avg `-0.0163` n `27`; metal avg `-0.0356` n `20`; unknown avg `57.7465` n `916`
- 4h: commodity avg `0.0328` n `12`; crypto_alt avg `-0.7898` n `233`; crypto_major avg `-1.0317` n `8`; equity avg `-0.1845` n `137`; fx avg `-0.0132` n `6`; index avg `0.0125` n `27`; metal avg `0.2373` n `20`; unknown avg `1.6485` n `901`
- 24h: commodity avg `0.5568` n `12`; crypto_alt avg `-3.8097` n `233`; crypto_major avg `-4.5725` n `8`; equity avg `-1.3214` n `137`; fx avg `0.2286` n `6`; index avg `-0.1481` n `27`; metal avg `0.1539` n `20`; unknown avg `2.6704` n `831`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
