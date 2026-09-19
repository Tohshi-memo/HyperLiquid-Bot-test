# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T06:37:32.612568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `0.4313` n `234`; crypto_major avg `0.2696` n `8`; equity avg `0.0236` n `140`; fx avg `-0.014` n `6`; index avg `-0.012` n `26`; metal avg `0.0037` n `20`; unknown avg `0.1306` n `942`
- 1h: commodity avg `-0.0095` n `12`; crypto_alt avg `-0.3666` n `234`; crypto_major avg `-0.2057` n `8`; equity avg `-0.0453` n `140`; fx avg `-0.0163` n `6`; index avg `-0.0364` n `26`; metal avg `-0.0094` n `20`; unknown avg `0.0429` n `904`
- 4h: commodity avg `-0.0326` n `12`; crypto_alt avg `-1.0423` n `234`; crypto_major avg `-0.5445` n `8`; equity avg `-0.1115` n `140`; fx avg `-0.0109` n `6`; index avg `-0.0292` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.2371` n `894`
- 24h: commodity avg `0.3105` n `12`; crypto_alt avg `3.3111` n `234`; crypto_major avg `4.4333` n `8`; equity avg `0.1303` n `140`; fx avg `0.0397` n `6`; index avg `-0.0867` n `26`; metal avg `-0.1343` n `20`; unknown avg `2.3682` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
