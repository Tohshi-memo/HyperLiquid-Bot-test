# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T12:07:23.175774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.1837` n `231`; crypto_major avg `-0.0241` n `8`; equity avg `-0.1178` n `122`; fx avg `-0.0062` n `6`; index avg `-0.0196` n `25`; metal avg `0.0438` n `20`; unknown avg `0.0798` n `793`
- 1h: commodity avg `0.1181` n `12`; crypto_alt avg `0.7916` n `231`; crypto_major avg `0.8607` n `8`; equity avg `0.271` n `122`; fx avg `-0.0126` n `6`; index avg `0.0483` n `25`; metal avg `0.0798` n `20`; unknown avg `0.3567` n `793`
- 4h: commodity avg `0.1343` n `12`; crypto_alt avg `0.6044` n `231`; crypto_major avg `0.8913` n `8`; equity avg `0.0426` n `122`; fx avg `-0.0176` n `6`; index avg `0.0321` n `25`; metal avg `0.0357` n `20`; unknown avg `0.6154` n `793`
- 24h: commodity avg `-0.0307` n `12`; crypto_alt avg `1.2298` n `231`; crypto_major avg `0.8413` n `8`; equity avg `-1.5049` n `122`; fx avg `-0.127` n `6`; index avg `-0.1417` n `25`; metal avg `0.1818` n `20`; unknown avg `4.4644` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
