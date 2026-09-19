# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T20:52:25.229516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `-0.1118` n `234`; crypto_major avg `-0.1061` n `8`; equity avg `0.0094` n `140`; fx avg `-0.0012` n `6`; index avg `-0.0021` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.1332` n `943`
- 1h: commodity avg `0.031` n `12`; crypto_alt avg `-0.3651` n `234`; crypto_major avg `-0.335` n `8`; equity avg `0.0346` n `140`; fx avg `-0.0498` n `6`; index avg `-0.0085` n `26`; metal avg `0.0018` n `20`; unknown avg `0.1456` n `927`
- 4h: commodity avg `0.0706` n `12`; crypto_alt avg `-0.4751` n `234`; crypto_major avg `-0.6566` n `8`; equity avg `0.1159` n `140`; fx avg `-0.055` n `6`; index avg `-0.0013` n `26`; metal avg `0.0122` n `20`; unknown avg `158.3371` n `887`
- 24h: commodity avg `0.0518` n `12`; crypto_alt avg `1.1868` n `234`; crypto_major avg `-0.0194` n `8`; equity avg `-0.027` n `140`; fx avg `-0.073` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0068` n `20`; unknown avg `2.578` n `820`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
