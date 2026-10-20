# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T04:41:35.872081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.1556` n `237`; crypto_major avg `-0.0646` n `8`; equity avg `-0.1038` n `151`; fx avg `-0.0086` n `6`; index avg `-0.0295` n `26`; metal avg `-0.0225` n `20`; unknown avg `-0.0871` n `1196`
- 1h: commodity avg `-0.0312` n `13`; crypto_alt avg `0.1261` n `237`; crypto_major avg `0.1755` n `8`; equity avg `-0.4176` n `151`; fx avg `-0.0151` n `6`; index avg `-0.084` n `26`; metal avg `-0.0137` n `20`; unknown avg `0.4117` n `1188`
- 4h: commodity avg `0.0537` n `13`; crypto_alt avg `0.7214` n `237`; crypto_major avg `0.4906` n `8`; equity avg `-0.2287` n `151`; fx avg `0.0109` n `6`; index avg `-0.087` n `26`; metal avg `0.1245` n `20`; unknown avg `1.4291` n `1188`
- 24h: commodity avg `0.2492` n `13`; crypto_alt avg `0.7986` n `237`; crypto_major avg `-0.0975` n `8`; equity avg `-1.1534` n `151`; fx avg `-0.0404` n `6`; index avg `-0.2101` n `26`; metal avg `-0.2231` n `20`; unknown avg `5.3569` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
