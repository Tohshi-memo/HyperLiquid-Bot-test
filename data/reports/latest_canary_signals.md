# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T20:52:29.697442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `13`; crypto_alt avg `-0.1562` n `235`; crypto_major avg `0.0674` n `8`; equity avg `0.0104` n `144`; fx avg `0.0064` n `6`; index avg `0.0026` n `26`; metal avg `0.0036` n `20`; unknown avg `19.4724` n `1078`
- 1h: commodity avg `0.008` n `13`; crypto_alt avg `-0.0862` n `235`; crypto_major avg `0.195` n `8`; equity avg `0.048` n `144`; fx avg `0.0143` n `6`; index avg `0.0092` n `26`; metal avg `-0.0053` n `20`; unknown avg `5.9418` n `1064`
- 4h: commodity avg `0.0968` n `13`; crypto_alt avg `0.2112` n `235`; crypto_major avg `0.3078` n `8`; equity avg `0.0576` n `144`; fx avg `0.0051` n `6`; index avg `0.0117` n `26`; metal avg `0.0203` n `20`; unknown avg `2.903` n `1064`
- 24h: commodity avg `0.0253` n `13`; crypto_alt avg `0.722` n `235`; crypto_major avg `1.1827` n `8`; equity avg `0.2175` n `144`; fx avg `0.0205` n `6`; index avg `-0.0091` n `26`; metal avg `0.014` n `20`; unknown avg `1.4394` n `1020`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
