# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T01:22:29.964854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `-0.5307` n `234`; crypto_major avg `-0.418` n `8`; equity avg `-0.0882` n `140`; fx avg `0.0144` n `6`; index avg `-0.0135` n `26`; metal avg `-0.004` n `20`; unknown avg `0.6131` n `942`
- 1h: commodity avg `0.0033` n `12`; crypto_alt avg `-0.6028` n `234`; crypto_major avg `-0.1163` n `8`; equity avg `-0.1233` n `140`; fx avg `-0.003` n `6`; index avg `0.0046` n `26`; metal avg `-0.0494` n `20`; unknown avg `-0.0484` n `940`
- 4h: commodity avg `0.1884` n `12`; crypto_alt avg `-0.3211` n `234`; crypto_major avg `-0.0902` n `8`; equity avg `-0.1074` n `140`; fx avg `-0.0224` n `6`; index avg `0.0045` n `26`; metal avg `-0.0343` n `20`; unknown avg `25.4623` n `908`
- 24h: commodity avg `0.115` n `12`; crypto_alt avg `5.5648` n `234`; crypto_major avg `5.9716` n `8`; equity avg `1.4241` n `140`; fx avg `0.1601` n `6`; index avg `0.1454` n `26`; metal avg `0.1311` n `20`; unknown avg `4.076` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
