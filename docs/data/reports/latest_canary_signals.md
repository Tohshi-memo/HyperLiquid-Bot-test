# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T17:07:28.148732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0243` n `13`; crypto_alt avg `-0.2299` n `235`; crypto_major avg `-0.1086` n `8`; equity avg `-0.1401` n `144`; fx avg `-0.0088` n `6`; index avg `-0.0193` n `26`; metal avg `-0.0189` n `20`; unknown avg `-0.068` n `1077`
- 1h: commodity avg `-0.0534` n `13`; crypto_alt avg `-0.2585` n `235`; crypto_major avg `-0.0044` n `8`; equity avg `-0.1148` n `144`; fx avg `-0.0063` n `6`; index avg `0.0153` n `26`; metal avg `-0.0251` n `20`; unknown avg `-0.2971` n `1077`
- 4h: commodity avg `-0.0596` n `13`; crypto_alt avg `-1.2342` n `235`; crypto_major avg `-0.6281` n `8`; equity avg `0.097` n `144`; fx avg `-0.0695` n `6`; index avg `0.1412` n `26`; metal avg `-0.1556` n `20`; unknown avg `0.7471` n `989`
- 24h: commodity avg `-0.2734` n `13`; crypto_alt avg `-0.3679` n `235`; crypto_major avg `-0.0462` n `8`; equity avg `0.1266` n `144`; fx avg `-0.1049` n `6`; index avg `0.0972` n `26`; metal avg `0.1164` n `20`; unknown avg `-0.326` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2006`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1776`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
