# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T12:07:27.150455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.03` n `13`; crypto_alt avg `-0.2782` n `235`; crypto_major avg `-0.0399` n `8`; equity avg `-0.0642` n `150`; fx avg `-0.0093` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0202` n `20`; unknown avg `-0.0423` n `1070`
- 1h: commodity avg `-0.0024` n `13`; crypto_alt avg `0.4403` n `235`; crypto_major avg `0.6568` n `8`; equity avg `0.151` n `150`; fx avg `0.0017` n `6`; index avg `0.0193` n `26`; metal avg `0.0497` n `20`; unknown avg `3.7784` n `1070`
- 4h: commodity avg `-0.031` n `13`; crypto_alt avg `-0.3631` n `235`; crypto_major avg `0.1417` n `8`; equity avg `0.0293` n `150`; fx avg `-0.0997` n `6`; index avg `-0.0159` n `26`; metal avg `-0.0746` n `20`; unknown avg `1.1005` n `1058`
- 24h: commodity avg `-0.5265` n `13`; crypto_alt avg `-0.8252` n `235`; crypto_major avg `-0.5944` n `8`; equity avg `-0.118` n `150`; fx avg `0.0209` n `6`; index avg `0.0547` n `26`; metal avg `0.497` n `20`; unknown avg `7.4793` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
