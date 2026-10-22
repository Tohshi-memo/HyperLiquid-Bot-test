# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T01:52:30.397131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3019` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0174` n `13`; crypto_alt avg `-0.5706` n `237`; crypto_major avg `-0.3918` n `8`; equity avg `-0.1612` n `151`; fx avg `-0.0296` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0484` n `20`; unknown avg `8.3351` n `1201`
- 1h: commodity avg `0.1244` n `13`; crypto_alt avg `-1.0338` n `237`; crypto_major avg `-1.0264` n `8`; equity avg `-0.6513` n `151`; fx avg `-0.0258` n `6`; index avg `-0.0755` n `26`; metal avg `-0.2692` n `20`; unknown avg `5.103` n `1193`
- 4h: commodity avg `0.2028` n `13`; crypto_alt avg `-1.6558` n `237`; crypto_major avg `-1.536` n `8`; equity avg `-1.6269` n `151`; fx avg `-0.0493` n `6`; index avg `-0.2341` n `26`; metal avg `-0.2778` n `20`; unknown avg `6.3691` n `1042`
- 24h: commodity avg `-0.5684` n `13`; crypto_alt avg `-0.0128` n `237`; crypto_major avg `-0.3576` n `8`; equity avg `-1.6681` n `151`; fx avg `-0.0368` n `6`; index avg `-0.2448` n `26`; metal avg `-0.3851` n `20`; unknown avg `120.2558` n `945`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
