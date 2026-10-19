# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T13:37:30.394191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0118` n `13`; crypto_alt avg `-0.2359` n `237`; crypto_major avg `-0.2846` n `8`; equity avg `-0.3045` n `151`; fx avg `0.0083` n `6`; index avg `-0.0104` n `26`; metal avg `0.0017` n `20`; unknown avg `0.0129` n `1195`
- 1h: commodity avg `-0.1209` n `13`; crypto_alt avg `-0.1411` n `237`; crypto_major avg `-0.3086` n `8`; equity avg `-0.1647` n `151`; fx avg `0.033` n `6`; index avg `0.009` n `26`; metal avg `-0.0343` n `20`; unknown avg `0.0417` n `1173`
- 4h: commodity avg `-0.099` n `13`; crypto_alt avg `-0.5147` n `237`; crypto_major avg `-0.6547` n `8`; equity avg `0.3759` n `151`; fx avg `0.0372` n `6`; index avg `0.0425` n `26`; metal avg `-0.0671` n `20`; unknown avg `0.6076` n `1151`
- 24h: commodity avg `-0.3487` n `13`; crypto_alt avg `0.451` n `237`; crypto_major avg `1.4153` n `8`; equity avg `3.13` n `151`; fx avg `-0.0208` n `6`; index avg `0.5325` n `26`; metal avg `0.1763` n `20`; unknown avg `2.1908` n `949`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2062`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1621`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1364`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0697`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0596`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
