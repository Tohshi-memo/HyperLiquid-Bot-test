# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T19:52:25.653065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2296` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0509` n `12`; crypto_alt avg `-0.3373` n `228`; crypto_major avg `-0.2905` n `8`; equity avg `-0.0242` n `88`; fx avg `-0.0104` n `6`; index avg `-0.0019` n `23`; metal avg `-0.0174` n `20`; unknown avg `0.0052` n `764`
- 1h: commodity avg `0.0963` n `12`; crypto_alt avg `-0.4625` n `228`; crypto_major avg `-0.5338` n `8`; equity avg `-0.0449` n `88`; fx avg `-0.017` n `6`; index avg `-0.0057` n `23`; metal avg `-0.0224` n `20`; unknown avg `-0.0519` n `764`
- 4h: commodity avg `0.0481` n `12`; crypto_alt avg `-1.3369` n `228`; crypto_major avg `-1.2556` n `8`; equity avg `-0.1298` n `88`; fx avg `-0.0422` n `6`; index avg `-0.026` n `23`; metal avg `0.0011` n `20`; unknown avg `-0.1354` n `764`
- 24h: commodity avg `0.3888` n `12`; crypto_alt avg `-0.5841` n `228`; crypto_major avg `-1.2548` n `8`; equity avg `0.131` n `88`; fx avg `-0.047` n `6`; index avg `-0.0331` n `23`; metal avg `-0.0049` n `20`; unknown avg `14.8613` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
