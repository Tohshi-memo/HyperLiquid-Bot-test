# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T13:52:23.672923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4892` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0695` n `13`; crypto_alt avg `0.0032` n `239`; crypto_major avg `-0.0677` n `8`; equity avg `-0.1081` n `162`; fx avg `-0.0097` n `6`; index avg `0.0154` n `27`; metal avg `-0.0705` n `20`; unknown avg `2.5179` n `1261`
- 1h: commodity avg `0.3607` n `13`; crypto_alt avg `-0.3817` n `239`; crypto_major avg `-0.6598` n `8`; equity avg `-0.6626` n `162`; fx avg `0.0121` n `6`; index avg `-0.0419` n `27`; metal avg `-0.2348` n `20`; unknown avg `1.8808` n `1253`
- 4h: commodity avg `0.2532` n `13`; crypto_alt avg `-1.2415` n `239`; crypto_major avg `-1.5795` n `8`; equity avg `-1.6934` n `162`; fx avg `-0.0005` n `6`; index avg `-0.0903` n `27`; metal avg `-0.3645` n `20`; unknown avg `19.4732` n `1247`
- 24h: commodity avg `0.1466` n `13`; crypto_alt avg `-3.3358` n `239`; crypto_major avg `-2.6252` n `8`; equity avg `-2.5079` n `162`; fx avg `-0.0955` n `6`; index avg `-0.1394` n `27`; metal avg `-1.1407` n `20`; unknown avg `0.7184` n `1138`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
