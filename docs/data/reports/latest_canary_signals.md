# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T06:31:12.316591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0449` n `12`; crypto_alt avg `0.0044` n `230`; crypto_major avg `0.0032` n `8`; equity avg `0.0658` n `92`; fx avg `0.0006` n `6`; index avg `-0.0135` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.0157` n `766`
- 1h: commodity avg `0.196` n `12`; crypto_alt avg `0.0782` n `230`; crypto_major avg `-0.0644` n `8`; equity avg `0.015` n `92`; fx avg `0.0152` n `6`; index avg `-0.0393` n `25`; metal avg `-0.0483` n `20`; unknown avg `-0.0055` n `750`
- 4h: commodity avg `0.1807` n `12`; crypto_alt avg `0.6481` n `230`; crypto_major avg `0.4799` n `8`; equity avg `1.146` n `92`; fx avg `-0.0091` n `6`; index avg `0.2806` n `25`; metal avg `0.2227` n `20`; unknown avg `0.0547` n `750`
- 24h: commodity avg `1.1124` n `12`; crypto_alt avg `-0.3982` n `230`; crypto_major avg `-0.3855` n `8`; equity avg `-0.0595` n `92`; fx avg `-0.135` n `6`; index avg `-0.0121` n `25`; metal avg `0.103` n `20`; unknown avg `-0.1751` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
