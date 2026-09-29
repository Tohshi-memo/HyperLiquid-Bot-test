# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T03:07:34.061161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `0.3884` n `234`; crypto_major avg `0.2461` n `8`; equity avg `-0.0037` n `141`; fx avg `-0.0003` n `6`; index avg `0.0032` n `26`; metal avg `0.0162` n `20`; unknown avg `0.0273` n `961`
- 1h: commodity avg `0.0608` n `12`; crypto_alt avg `-0.2481` n `234`; crypto_major avg `0.0038` n `8`; equity avg `-0.0606` n `141`; fx avg `-0.0086` n `6`; index avg `-0.0356` n `26`; metal avg `0.0456` n `20`; unknown avg `-0.3729` n `961`
- 4h: commodity avg `0.1052` n `12`; crypto_alt avg `-1.7644` n `234`; crypto_major avg `-0.9281` n `8`; equity avg `-0.5136` n `141`; fx avg `-0.0295` n `6`; index avg `-0.0928` n `26`; metal avg `-0.0069` n `20`; unknown avg `0.7481` n `955`
- 24h: commodity avg `0.2119` n `12`; crypto_alt avg `-3.7522` n `234`; crypto_major avg `-1.7072` n `8`; equity avg `-2.2412` n `141`; fx avg `-0.0422` n `6`; index avg `-0.2214` n `26`; metal avg `-0.4693` n `20`; unknown avg `9.7617` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
