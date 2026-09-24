# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T04:52:34.718599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `0.223` n `234`; crypto_major avg `0.1198` n `8`; equity avg `-0.013` n `141`; fx avg `0.008` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0048` n `20`; unknown avg `-0.2532` n `945`
- 1h: commodity avg `0.0436` n `12`; crypto_alt avg `0.6489` n `234`; crypto_major avg `0.2203` n `8`; equity avg `-0.0984` n `141`; fx avg `0.0086` n `6`; index avg `-0.004` n `26`; metal avg `0.0393` n `20`; unknown avg `0.845` n `937`
- 4h: commodity avg `0.0237` n `12`; crypto_alt avg `1.2162` n `234`; crypto_major avg `-0.1236` n `8`; equity avg `-0.237` n `141`; fx avg `-0.0403` n `6`; index avg `-0.0309` n `26`; metal avg `0.0322` n `20`; unknown avg `2.0246` n `937`
- 24h: commodity avg `0.6058` n `12`; crypto_alt avg `-4.4229` n `234`; crypto_major avg `-4.9277` n `8`; equity avg `-2.027` n `140`; fx avg `0.1313` n `6`; index avg `-0.3702` n `26`; metal avg `-0.6441` n `20`; unknown avg `585.4679` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
