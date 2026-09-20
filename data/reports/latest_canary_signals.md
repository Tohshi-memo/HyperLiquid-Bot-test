# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T13:52:26.998584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0436` n `12`; crypto_alt avg `0.0976` n `234`; crypto_major avg `0.1598` n `8`; equity avg `-0.0059` n `140`; fx avg `0.0032` n `6`; index avg `-0.0032` n `26`; metal avg `0.0058` n `20`; unknown avg `-0.0192` n `943`
- 1h: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.2904` n `234`; crypto_major avg `-0.0354` n `8`; equity avg `-0.005` n `140`; fx avg `-0.0013` n `6`; index avg `0.0065` n `26`; metal avg `0.0101` n `20`; unknown avg `1.0446` n `941`
- 4h: commodity avg `0.0518` n `12`; crypto_alt avg `-0.4993` n `234`; crypto_major avg `-0.1082` n `8`; equity avg `-0.0183` n `140`; fx avg `-0.009` n `6`; index avg `0.0079` n `26`; metal avg `-0.0316` n `20`; unknown avg `1.1454` n `935`
- 24h: commodity avg `0.2651` n `12`; crypto_alt avg `-2.2858` n `234`; crypto_major avg `-2.2634` n `8`; equity avg `-0.3037` n `140`; fx avg `-0.0536` n `6`; index avg `-0.0492` n `26`; metal avg `-0.0236` n `20`; unknown avg `1.26` n `818`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
