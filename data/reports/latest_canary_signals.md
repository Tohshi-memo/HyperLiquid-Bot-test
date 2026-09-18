# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T20:37:27.569960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `0.0585` n `234`; crypto_major avg `-0.3352` n `8`; equity avg `-0.0627` n `140`; fx avg `0.0023` n `6`; index avg `-0.003` n `26`; metal avg `-0.0183` n `20`; unknown avg `-0.2571` n `934`
- 1h: commodity avg `-0.0213` n `12`; crypto_alt avg `0.2922` n `234`; crypto_major avg `-0.1967` n `8`; equity avg `0.3021` n `140`; fx avg `0.0108` n `6`; index avg `0.0786` n `26`; metal avg `-0.0012` n `20`; unknown avg `62.3208` n `896`
- 4h: commodity avg `-0.1134` n `12`; crypto_alt avg `0.8568` n `234`; crypto_major avg `0.3722` n `8`; equity avg `0.8824` n `140`; fx avg `0.0273` n `6`; index avg `0.1945` n `26`; metal avg `-0.0166` n `20`; unknown avg `5.9062` n `878`
- 24h: commodity avg `-0.1229` n `12`; crypto_alt avg `6.7429` n `234`; crypto_major avg `6.6997` n `8`; equity avg `1.2617` n `140`; fx avg `0.2167` n `6`; index avg `0.0601` n `26`; metal avg `0.4134` n `20`; unknown avg `8.2039` n `727`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
