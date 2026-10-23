# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T22:52:28.497500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3198` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0374` n `13`; crypto_alt avg `-0.9302` n `237`; crypto_major avg `-0.504` n `8`; equity avg `-0.1656` n `152`; fx avg `-0.0202` n `6`; index avg `-0.0222` n `26`; metal avg `-0.0776` n `20`; unknown avg `0.2659` n `1230`
- 1h: commodity avg `0.0255` n `13`; crypto_alt avg `-1.793` n `237`; crypto_major avg `-1.0455` n `8`; equity avg `-0.3323` n `152`; fx avg `0.0242` n `6`; index avg `-0.0485` n `26`; metal avg `-0.111` n `20`; unknown avg `13.496` n `1222`
- 4h: commodity avg `0.176` n `13`; crypto_alt avg `-2.706` n `237`; crypto_major avg `-1.3592` n `8`; equity avg `-0.5695` n `152`; fx avg `0.0271` n `6`; index avg `-0.0394` n `26`; metal avg `-0.147` n `20`; unknown avg `0.6225` n `1134`
- 24h: commodity avg `0.5461` n `13`; crypto_alt avg `-1.4772` n `237`; crypto_major avg `-0.634` n `8`; equity avg `1.0476` n `152`; fx avg `-0.044` n `6`; index avg `0.0486` n `26`; metal avg `-0.2604` n `20`; unknown avg `199.5058` n `1024`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
