# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T04:52:28.813789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.023` n `13`; crypto_alt avg `-0.1666` n `235`; crypto_major avg `-0.159` n `8`; equity avg `-0.0871` n `150`; fx avg `0.019` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0458` n `20`; unknown avg `1.1366` n `1078`
- 1h: commodity avg `-0.0015` n `13`; crypto_alt avg `-0.0151` n `235`; crypto_major avg `-0.1206` n `8`; equity avg `0.0388` n `150`; fx avg `0.0038` n `6`; index avg `0.0129` n `26`; metal avg `-0.0137` n `20`; unknown avg `-0.2022` n `1068`
- 4h: commodity avg `-0.2393` n `13`; crypto_alt avg `1.241` n `235`; crypto_major avg `0.4339` n `8`; equity avg `0.3798` n `150`; fx avg `-0.0291` n `6`; index avg `0.0693` n `26`; metal avg `0.3158` n `20`; unknown avg `0.8301` n `1068`
- 24h: commodity avg `0.1044` n `13`; crypto_alt avg `-1.256` n `235`; crypto_major avg `-2.1395` n `8`; equity avg `-1.8205` n `150`; fx avg `0.1025` n `6`; index avg `-0.1801` n `26`; metal avg `0.1063` n `20`; unknown avg `5.6089` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
