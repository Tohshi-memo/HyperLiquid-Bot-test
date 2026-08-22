# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T01:52:26.285968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `-0.3208` n `230`; crypto_major avg `-0.5149` n `8`; equity avg `-0.0046` n `121`; fx avg `0.0068` n `6`; index avg `0.0007` n `25`; metal avg `0.0027` n `20`; unknown avg `0.0189` n `793`
- 1h: commodity avg `0.0287` n `12`; crypto_alt avg `0.1718` n `230`; crypto_major avg `0.4437` n `8`; equity avg `-0.0401` n `121`; fx avg `0.0133` n `6`; index avg `-0.005` n `25`; metal avg `-0.0114` n `20`; unknown avg `0.5363` n `793`
- 4h: commodity avg `-0.0166` n `12`; crypto_alt avg `1.148` n `230`; crypto_major avg `0.516` n `8`; equity avg `-0.0153` n `121`; fx avg `0.0014` n `6`; index avg `0.017` n `25`; metal avg `-0.0339` n `20`; unknown avg `0.8508` n `793`
- 24h: commodity avg `0.0265` n `12`; crypto_alt avg `8.5191` n `230`; crypto_major avg `5.6221` n `8`; equity avg `0.2993` n `121`; fx avg `0.0502` n `6`; index avg `0.0359` n `25`; metal avg `0.3179` n `20`; unknown avg `1.7552` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
