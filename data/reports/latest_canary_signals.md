# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T04:07:29.062181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.0226` n `234`; crypto_major avg `0.0421` n `8`; equity avg `0.012` n `140`; fx avg `-0.0077` n `6`; index avg `-0.001` n `26`; metal avg `0.0017` n `20`; unknown avg `-0.178` n `914`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.2904` n `234`; crypto_major avg `-0.2079` n `8`; equity avg `-0.0168` n `140`; fx avg `-0.0048` n `6`; index avg `0.0152` n `26`; metal avg `-0.0119` n `20`; unknown avg `-0.3714` n `914`
- 4h: commodity avg `-0.0003` n `12`; crypto_alt avg `0.5127` n `234`; crypto_major avg `0.6334` n `8`; equity avg `-0.1147` n `140`; fx avg `-0.0255` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0138` n `20`; unknown avg `0.2772` n `914`
- 24h: commodity avg `0.1315` n `12`; crypto_alt avg `4.3955` n `234`; crypto_major avg `5.1841` n `8`; equity avg `0.6956` n `140`; fx avg `0.0316` n `6`; index avg `0.0181` n `26`; metal avg `0.0695` n `20`; unknown avg `2.3942` n `767`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
