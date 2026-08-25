# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T17:52:26.247627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `12`; crypto_alt avg `0.031` n `231`; crypto_major avg `0.0406` n `8`; equity avg `-0.0195` n `122`; fx avg `-0.0013` n `6`; index avg `-0.0004` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0415` n `795`
- 1h: commodity avg `-0.0141` n `12`; crypto_alt avg `-0.331` n `231`; crypto_major avg `-0.127` n `8`; equity avg `-0.0987` n `122`; fx avg `0.0129` n `6`; index avg `-0.0244` n `25`; metal avg `-0.0188` n `20`; unknown avg `-0.2597` n `795`
- 4h: commodity avg `0.1023` n `12`; crypto_alt avg `0.9081` n `231`; crypto_major avg `1.3827` n `8`; equity avg `0.0233` n `122`; fx avg `-0.0168` n `6`; index avg `-0.0738` n `25`; metal avg `0.3313` n `20`; unknown avg `0.226` n `795`
- 24h: commodity avg `-0.574` n `12`; crypto_alt avg `-0.2058` n `231`; crypto_major avg `1.0786` n `8`; equity avg `1.7314` n `122`; fx avg `0.0561` n `6`; index avg `0.2208` n `25`; metal avg `0.0073` n `20`; unknown avg `-0.642` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
