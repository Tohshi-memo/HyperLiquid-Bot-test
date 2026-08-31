# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T12:07:30.787966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1064` n `12`; crypto_alt avg `0.2396` n `232`; crypto_major avg `0.2235` n `8`; equity avg `0.1137` n `128`; fx avg `0.0084` n `6`; index avg `0.022` n `26`; metal avg `0.0323` n `20`; unknown avg `-0.0995` n `792`
- 1h: commodity avg `0.005` n `12`; crypto_alt avg `0.0306` n `232`; crypto_major avg `-0.1339` n `8`; equity avg `0.0313` n `128`; fx avg `-0.0005` n `6`; index avg `0.0087` n `26`; metal avg `0.0298` n `20`; unknown avg `0.0504` n `792`
- 4h: commodity avg `0.2895` n `12`; crypto_alt avg `0.2487` n `232`; crypto_major avg `0.6301` n `8`; equity avg `-0.2409` n `128`; fx avg `-0.0161` n `6`; index avg `-0.0436` n `26`; metal avg `0.0749` n `20`; unknown avg `0.1856` n `791`
- 24h: commodity avg `0.6232` n `12`; crypto_alt avg `-0.6697` n `231`; crypto_major avg `-1.1387` n `8`; equity avg `-0.4398` n `128`; fx avg `-0.1385` n `6`; index avg `-0.0741` n `26`; metal avg `-0.098` n `20`; unknown avg `-0.0193` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
