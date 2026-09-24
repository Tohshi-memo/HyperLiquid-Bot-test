# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T08:07:38.194714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1993` n `12`; crypto_alt avg `-0.0338` n `234`; crypto_major avg `-0.1669` n `8`; equity avg `-0.2208` n `141`; fx avg `0.0093` n `6`; index avg `-0.0495` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.5659` n `937`
- 1h: commodity avg `0.1594` n `12`; crypto_alt avg `0.4182` n `234`; crypto_major avg `0.4623` n `8`; equity avg `-0.0256` n `141`; fx avg `-0.0386` n `6`; index avg `-0.0089` n `26`; metal avg `0.0642` n `20`; unknown avg `0.7438` n `937`
- 4h: commodity avg `0.364` n `12`; crypto_alt avg `1.1514` n `234`; crypto_major avg `0.899` n `8`; equity avg `-0.1873` n `141`; fx avg `-0.0034` n `6`; index avg `-0.0549` n `26`; metal avg `0.1052` n `20`; unknown avg `1.7193` n `921`
- 24h: commodity avg `0.7193` n `12`; crypto_alt avg `-2.8937` n `234`; crypto_major avg `-2.8289` n `8`; equity avg `-2.078` n `140`; fx avg `-0.048` n `6`; index avg `-0.4235` n `26`; metal avg `-0.3312` n `20`; unknown avg `587.8818` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
