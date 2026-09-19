# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T05:37:31.035620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0897` n `234`; crypto_major avg `0.1501` n `8`; equity avg `0.0051` n `140`; fx avg `0.0241` n `6`; index avg `0.0175` n `26`; metal avg `0.0092` n `20`; unknown avg `58.0481` n `942`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.0369` n `234`; crypto_major avg `0.469` n `8`; equity avg `-0.0005` n `140`; fx avg `0.0112` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0005` n `20`; unknown avg `3.1143` n `940`
- 4h: commodity avg `-0.0247` n `12`; crypto_alt avg `0.3855` n `234`; crypto_major avg `0.4808` n `8`; equity avg `-0.0581` n `140`; fx avg `0.001` n `6`; index avg `-0.0088` n `26`; metal avg `0.0101` n `20`; unknown avg `0.5556` n `914`
- 24h: commodity avg `0.1681` n `12`; crypto_alt avg `3.811` n `234`; crypto_major avg `4.5771` n `8`; equity avg `0.4339` n `140`; fx avg `0.0462` n `6`; index avg `-0.0086` n `26`; metal avg `0.0047` n `20`; unknown avg `2.3339` n `767`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
