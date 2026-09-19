# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T04:52:26.686592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `-0.2162` n `234`; crypto_major avg `0.0156` n `8`; equity avg `-0.0217` n `140`; fx avg `-0.009` n `6`; index avg `0.0016` n `26`; metal avg `-0.01` n `20`; unknown avg `0.0762` n `942`
- 1h: commodity avg `-0.0315` n `12`; crypto_alt avg `-0.8374` n `234`; crypto_major avg `-0.4582` n `8`; equity avg `-0.063` n `140`; fx avg `-0.018` n `6`; index avg `0.0057` n `26`; metal avg `-0.0089` n `20`; unknown avg `-0.166` n `914`
- 4h: commodity avg `-0.0429` n `12`; crypto_alt avg `-0.504` n `234`; crypto_major avg `-0.3912` n `8`; equity avg `-0.2234` n `140`; fx avg `-0.0209` n `6`; index avg `0.0068` n `26`; metal avg `-0.0217` n `20`; unknown avg `0.4178` n `914`
- 24h: commodity avg `0.1303` n `12`; crypto_alt avg `3.4567` n `234`; crypto_major avg `4.3689` n `8`; equity avg `0.5094` n `140`; fx avg `0.0134` n `6`; index avg `0.0131` n `26`; metal avg `0.0451` n `20`; unknown avg `2.4222` n `767`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
