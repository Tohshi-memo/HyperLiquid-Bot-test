# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T05:37:29.333597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `0.0297` n `233`; crypto_major avg `0.0722` n `8`; equity avg `0.1308` n `136`; fx avg `0.0008` n `6`; index avg `0.0363` n `27`; metal avg `-0.0135` n `20`; unknown avg `1.4878` n `908`
- 1h: commodity avg `0.0386` n `12`; crypto_alt avg `-0.252` n `233`; crypto_major avg `-0.2676` n `8`; equity avg `-0.1048` n `136`; fx avg `0.0533` n `6`; index avg `-0.0094` n `27`; metal avg `-0.0465` n `20`; unknown avg `7.4941` n `906`
- 4h: commodity avg `0.1488` n `12`; crypto_alt avg `-0.9233` n `233`; crypto_major avg `-0.8875` n `8`; equity avg `-0.6137` n `136`; fx avg `0.0922` n `6`; index avg `-0.1125` n `27`; metal avg `0.0228` n `20`; unknown avg `7.8935` n `890`
- 24h: commodity avg `0.1252` n `12`; crypto_alt avg `-1.258` n `233`; crypto_major avg `-0.3731` n `8`; equity avg `-0.5082` n `136`; fx avg `0.155` n `6`; index avg `-0.1039` n `27`; metal avg `-0.3487` n `20`; unknown avg `6.0887` n `788`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
