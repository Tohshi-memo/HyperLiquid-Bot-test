# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T16:07:36.381250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0983` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0653` n `12`; crypto_alt avg `0.0352` n `230`; crypto_major avg `-0.0154` n `8`; equity avg `0.0072` n `113`; fx avg `-0.0073` n `6`; index avg `0.0089` n `25`; metal avg `0.0868` n `20`; unknown avg `0.0025` n `785`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `-0.1572` n `230`; crypto_major avg `-0.3306` n `8`; equity avg `0.0391` n `113`; fx avg `-0.006` n `6`; index avg `0.007` n `25`; metal avg `0.1179` n `20`; unknown avg `1.8003` n `784`
- 4h: commodity avg `0.4189` n `12`; crypto_alt avg `-0.7015` n `230`; crypto_major avg `-1.1003` n `8`; equity avg `-0.5277` n `113`; fx avg `0.0624` n `6`; index avg `-0.002` n `25`; metal avg `0.2232` n `20`; unknown avg `1.7369` n `784`
- 24h: commodity avg `1.0509` n `12`; crypto_alt avg `-0.5225` n `230`; crypto_major avg `-1.4656` n `8`; equity avg `-1.0305` n `113`; fx avg `0.2455` n `6`; index avg `-0.0122` n `25`; metal avg `0.0559` n `20`; unknown avg `103.596` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
