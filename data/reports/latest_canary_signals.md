# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T11:22:29.394533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0302` n `13`; crypto_alt avg `0.0921` n `239`; crypto_major avg `0.023` n `8`; equity avg `-0.1348` n `166`; fx avg `-0.0052` n `6`; index avg `-0.0104` n `27`; metal avg `-0.0101` n `20`; unknown avg `12.6593` n `1264`
- 1h: commodity avg `-0.2369` n `13`; crypto_alt avg `0.0272` n `239`; crypto_major avg `0.2008` n `8`; equity avg `-0.2437` n `166`; fx avg `-0.01` n `6`; index avg `-0.0075` n `27`; metal avg `0.0198` n `20`; unknown avg `9.9452` n `1262`
- 4h: commodity avg `-0.3401` n `13`; crypto_alt avg `0.0455` n `239`; crypto_major avg `0.1475` n `8`; equity avg `0.5842` n `166`; fx avg `-0.0473` n `6`; index avg `0.0678` n `27`; metal avg `-0.104` n `20`; unknown avg `240.8289` n `1106`
- 24h: commodity avg `-0.9681` n `13`; crypto_alt avg `0.5519` n `239`; crypto_major avg `0.97` n `8`; equity avg `1.9675` n `166`; fx avg `0.1906` n `6`; index avg `0.1315` n `27`; metal avg `0.4077` n `20`; unknown avg `2.5748` n `1059`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
