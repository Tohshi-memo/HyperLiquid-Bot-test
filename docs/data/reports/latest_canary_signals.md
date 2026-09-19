# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T07:07:29.361653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `0.0199` n `234`; crypto_major avg `0.0135` n `8`; equity avg `0.0215` n `140`; fx avg `0.0262` n `6`; index avg `0.0247` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.0472` n `940`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `0.2254` n `234`; crypto_major avg `-0.0218` n `8`; equity avg `0.0204` n `140`; fx avg `0.0251` n `6`; index avg `0.0185` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.1097` n `940`
- 4h: commodity avg `-0.0412` n `12`; crypto_alt avg `-1.213` n `234`; crypto_major avg `-0.5544` n `8`; equity avg `-0.1137` n `140`; fx avg `0.0122` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0247` n `20`; unknown avg `0.057` n `894`
- 24h: commodity avg `0.2375` n `12`; crypto_alt avg `3.145` n `234`; crypto_major avg `4.0734` n `8`; equity avg `0.0674` n `140`; fx avg `0.1024` n `6`; index avg `-0.0706` n `26`; metal avg `-0.1718` n `20`; unknown avg `2.3577` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
