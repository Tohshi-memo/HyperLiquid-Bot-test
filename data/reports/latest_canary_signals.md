# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T05:52:30.717854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0854` n `13`; crypto_alt avg `-0.0429` n `234`; crypto_major avg `0.0466` n `8`; equity avg `0.0317` n `142`; fx avg `0.0252` n `6`; index avg `-0.0032` n `26`; metal avg `-0.039` n `20`; unknown avg `5.9252` n `974`
- 1h: commodity avg `0.2685` n `13`; crypto_alt avg `-0.0657` n `234`; crypto_major avg `0.021` n `8`; equity avg `0.2803` n `142`; fx avg `0.0266` n `6`; index avg `0.074` n `26`; metal avg `0.0646` n `20`; unknown avg `0.4511` n `972`
- 4h: commodity avg `-0.1905` n `13`; crypto_alt avg `1.0657` n `234`; crypto_major avg `0.6859` n `8`; equity avg `1.0242` n `142`; fx avg `-0.0285` n `6`; index avg `0.2299` n `26`; metal avg `0.1848` n `20`; unknown avg `0.8825` n `966`
- 24h: commodity avg `-0.3512` n `13`; crypto_alt avg `1.1518` n `234`; crypto_major avg `1.3313` n `8`; equity avg `1.0481` n `142`; fx avg `0.1809` n `6`; index avg `0.2817` n `26`; metal avg `0.0899` n `20`; unknown avg `778.5935` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
