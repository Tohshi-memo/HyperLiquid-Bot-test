# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T21:37:29.128501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0239` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `0.3717` n `235`; crypto_major avg `0.1777` n `8`; equity avg `0.0189` n `150`; fx avg `-0.0054` n `6`; index avg `-0.0024` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.0249` n `1134`
- 1h: commodity avg `0.034` n `13`; crypto_alt avg `-0.5686` n `235`; crypto_major avg `-0.3735` n `8`; equity avg `-0.0589` n `150`; fx avg `-0.0177` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0215` n `20`; unknown avg `0.2898` n `1122`
- 4h: commodity avg `0.128` n `13`; crypto_alt avg `-0.7925` n `235`; crypto_major avg `-1.041` n `8`; equity avg `-0.1006` n `150`; fx avg `-0.0163` n `6`; index avg `-0.0171` n `26`; metal avg `-0.0246` n `20`; unknown avg `0.9834` n `1098`
- 24h: commodity avg `0.3354` n `13`; crypto_alt avg `1.1149` n `235`; crypto_major avg `0.2422` n `8`; equity avg `0.1995` n `150`; fx avg `0.0117` n `6`; index avg `0.025` n `26`; metal avg `0.0642` n `20`; unknown avg `0.6031` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
