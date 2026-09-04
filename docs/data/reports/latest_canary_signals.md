# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T06:22:22.948493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0424` n `12`; crypto_alt avg `-0.1272` n `232`; crypto_major avg `-0.1285` n `8`; equity avg `-0.0419` n `133`; fx avg `0.0008` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0312` n `20`; unknown avg `0.38` n `793`
- 1h: commodity avg `-0.05` n `12`; crypto_alt avg `-0.4978` n `232`; crypto_major avg `-0.2462` n `8`; equity avg `-0.2158` n `133`; fx avg `-0.0017` n `6`; index avg `-0.0368` n `26`; metal avg `-0.0393` n `20`; unknown avg `1.6909` n `757`
- 4h: commodity avg `-0.0834` n `12`; crypto_alt avg `-0.4681` n `232`; crypto_major avg `0.0509` n `8`; equity avg `0.2339` n `133`; fx avg `-0.0377` n `6`; index avg `0.068` n `26`; metal avg `-0.0724` n `20`; unknown avg `1.4371` n `757`
- 24h: commodity avg `-0.0653` n `12`; crypto_alt avg `1.7045` n `232`; crypto_major avg `3.8172` n `8`; equity avg `1.8786` n `133`; fx avg `-0.0985` n `6`; index avg `0.3363` n `26`; metal avg `0.4654` n `20`; unknown avg `2.2702` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
