# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T09:22:35.167800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `-0.0483` n `234`; crypto_major avg `0.0872` n `8`; equity avg `0.0183` n `140`; fx avg `-0.0037` n `6`; index avg `0.0036` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.0656` n `944`
- 1h: commodity avg `-0.2751` n `12`; crypto_alt avg `-0.047` n `234`; crypto_major avg `0.3004` n `8`; equity avg `0.4358` n `140`; fx avg `-0.0887` n `6`; index avg `0.0698` n `26`; metal avg `0.1526` n `20`; unknown avg `0.5075` n `942`
- 4h: commodity avg `-0.3383` n `12`; crypto_alt avg `0.6491` n `234`; crypto_major avg `0.6616` n `8`; equity avg `-0.0517` n `140`; fx avg `-0.0619` n `6`; index avg `-0.0174` n `26`; metal avg `-0.1046` n `20`; unknown avg `9.3758` n `908`
- 24h: commodity avg `-0.5028` n `12`; crypto_alt avg `1.0031` n `234`; crypto_major avg `1.972` n `8`; equity avg `0.6857` n `140`; fx avg `-0.2555` n `6`; index avg `0.2222` n `26`; metal avg `-0.219` n `20`; unknown avg `1120.2403` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
