# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T07:22:27.937131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0515` n `13`; crypto_alt avg `-0.0989` n `237`; crypto_major avg `-0.0729` n `8`; equity avg `-0.1356` n `151`; fx avg `0.0037` n `6`; index avg `-0.045` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.5961` n `1198`
- 1h: commodity avg `0.1007` n `13`; crypto_alt avg `0.0316` n `237`; crypto_major avg `-0.0324` n `8`; equity avg `0.0565` n `151`; fx avg `-0.0236` n `6`; index avg `0.0037` n `26`; metal avg `0.0655` n `20`; unknown avg `0.3758` n `1196`
- 4h: commodity avg `0.0342` n `13`; crypto_alt avg `-0.1413` n `237`; crypto_major avg `-0.2422` n `8`; equity avg `-0.6251` n `151`; fx avg `-0.0124` n `6`; index avg `-0.0797` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.3476` n `1168`
- 24h: commodity avg `0.4159` n `13`; crypto_alt avg `-0.1903` n `237`; crypto_major avg `-0.9516` n `8`; equity avg `-1.4821` n `151`; fx avg `0.0131` n `6`; index avg `-0.2242` n `26`; metal avg `-0.2301` n `20`; unknown avg `4.9852` n `1013`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
