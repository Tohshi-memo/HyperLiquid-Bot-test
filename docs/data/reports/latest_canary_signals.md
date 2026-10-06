# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T06:22:31.260438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1832` n `13`; crypto_alt avg `0.121` n `235`; crypto_major avg `0.0463` n `8`; equity avg `0.0392` n `149`; fx avg `0.026` n `6`; index avg `0.015` n `26`; metal avg `0.1111` n `20`; unknown avg `0.851` n `1070`
- 1h: commodity avg `-0.2646` n `13`; crypto_alt avg `-0.4156` n `235`; crypto_major avg `-0.4669` n `8`; equity avg `0.0693` n `149`; fx avg `-0.0034` n `6`; index avg `0.0323` n `26`; metal avg `0.0299` n `20`; unknown avg `4.4623` n `1044`
- 4h: commodity avg `-0.2023` n `13`; crypto_alt avg `-0.5197` n `235`; crypto_major avg `-0.6151` n `8`; equity avg `0.0708` n `149`; fx avg `-0.0001` n `6`; index avg `0.0389` n `26`; metal avg `-0.0466` n `20`; unknown avg `4.5126` n `1036`
- 24h: commodity avg `-0.1971` n `13`; crypto_alt avg `-1.1852` n `235`; crypto_major avg `-0.7205` n `8`; equity avg `0.1715` n `149`; fx avg `0.0477` n `6`; index avg `0.1551` n `26`; metal avg `-0.1342` n `20`; unknown avg `587.267` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
