# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T06:37:27.916175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `0.0763` n `234`; crypto_major avg `-0.0338` n `8`; equity avg `-0.003` n `141`; fx avg `-0.0007` n `6`; index avg `0.0023` n `26`; metal avg `0.002` n `20`; unknown avg `-0.0314` n `961`
- 1h: commodity avg `0.0042` n `12`; crypto_alt avg `0.2882` n `234`; crypto_major avg `0.0864` n `8`; equity avg `0.001` n `141`; fx avg `-0.0037` n `6`; index avg `0.0056` n `26`; metal avg `-0.0033` n `20`; unknown avg `1.9837` n `939`
- 4h: commodity avg `0.0689` n `12`; crypto_alt avg `0.3076` n `234`; crypto_major avg `0.058` n `8`; equity avg `0.0359` n `141`; fx avg `0.0091` n `6`; index avg `0.0166` n `26`; metal avg `-0.0161` n `20`; unknown avg `-0.0813` n `933`
- 24h: commodity avg `0.0138` n `12`; crypto_alt avg `1.018` n `234`; crypto_major avg `0.3043` n `8`; equity avg `0.29` n `141`; fx avg `0.0324` n `6`; index avg `0.0066` n `26`; metal avg `-0.0214` n `20`; unknown avg `4.7768` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
