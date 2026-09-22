# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T18:52:35.443026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0428` n `12`; crypto_alt avg `-0.0038` n `234`; crypto_major avg `0.1696` n `8`; equity avg `-0.0152` n `140`; fx avg `-0.0003` n `6`; index avg `0.0002` n `26`; metal avg `0.0299` n `20`; unknown avg `-0.0684` n `942`
- 1h: commodity avg `0.0924` n `12`; crypto_alt avg `-0.1552` n `234`; crypto_major avg `0.0243` n `8`; equity avg `-0.0089` n `140`; fx avg `0.0209` n `6`; index avg `0.0007` n `26`; metal avg `0.1439` n `20`; unknown avg `0.3558` n `940`
- 4h: commodity avg `0.0342` n `12`; crypto_alt avg `1.577` n `234`; crypto_major avg `0.9136` n `8`; equity avg `0.4101` n `140`; fx avg `0.0012` n `6`; index avg `0.0648` n `26`; metal avg `0.3142` n `20`; unknown avg `0.2669` n `880`
- 24h: commodity avg `0.1578` n `12`; crypto_alt avg `2.0677` n `234`; crypto_major avg `0.9502` n `8`; equity avg `0.6614` n `140`; fx avg `-0.2729` n `6`; index avg `0.0818` n `26`; metal avg `0.2258` n `20`; unknown avg `0.9276` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
