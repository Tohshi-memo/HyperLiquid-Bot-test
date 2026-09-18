# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T20:07:27.108942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `-0.0366` n `234`; crypto_major avg `-0.1165` n `8`; equity avg `0.1984` n `140`; fx avg `-0.0033` n `6`; index avg `0.0354` n `26`; metal avg `0.0058` n `20`; unknown avg `27.0986` n `918`
- 1h: commodity avg `0.0548` n `12`; crypto_alt avg `0.2396` n `234`; crypto_major avg `0.4559` n `8`; equity avg `0.4634` n `140`; fx avg `0.0107` n `6`; index avg `0.0768` n `26`; metal avg `-0.0059` n `20`; unknown avg `390.183` n `918`
- 4h: commodity avg `-0.1964` n `12`; crypto_alt avg `0.7811` n `234`; crypto_major avg `0.8761` n `8`; equity avg `0.8329` n `140`; fx avg `0.0258` n `6`; index avg `0.1805` n `26`; metal avg `0.0938` n `20`; unknown avg `15.0922` n `900`
- 24h: commodity avg `-0.03` n `12`; crypto_alt avg `6.6661` n `234`; crypto_major avg `7.0762` n `8`; equity avg `1.3221` n `140`; fx avg `0.2052` n `6`; index avg `0.0422` n `26`; metal avg `0.3823` n `20`; unknown avg `9.5899` n `727`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
