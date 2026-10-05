# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T16:22:31.946632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1755` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.002` n `13`; crypto_alt avg `-0.3506` n `235`; crypto_major avg `-0.3452` n `8`; equity avg `-0.1069` n `144`; fx avg `0.0007` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0301` n `20`; unknown avg `1.9537` n `1079`
- 1h: commodity avg `-0.2128` n `13`; crypto_alt avg `-0.5053` n `235`; crypto_major avg `-0.5318` n `8`; equity avg `-0.002` n `144`; fx avg `-0.0116` n `6`; index avg `0.0219` n `26`; metal avg `0.0008` n `20`; unknown avg `1.5124` n `1071`
- 4h: commodity avg `-0.1176` n `13`; crypto_alt avg `-1.4506` n `235`; crypto_major avg `-1.0833` n `8`; equity avg `0.0996` n `144`; fx avg `-0.0332` n `6`; index avg `0.0922` n `26`; metal avg `-0.1974` n `20`; unknown avg `0.6944` n `989`
- 24h: commodity avg `-0.1815` n `13`; crypto_alt avg `-0.3144` n `235`; crypto_major avg `-0.1847` n `8`; equity avg `0.1493` n `144`; fx avg `-0.1064` n `6`; index avg `0.0771` n `26`; metal avg `0.111` n `20`; unknown avg `-0.1539` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2021`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
