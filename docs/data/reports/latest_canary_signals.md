# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T07:52:26.530674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0321` n `12`; crypto_alt avg `-0.1542` n `230`; crypto_major avg `-0.2133` n `8`; equity avg `-0.0307` n `92`; fx avg `-0.0164` n `6`; index avg `-0.0094` n `25`; metal avg `-0.0135` n `20`; unknown avg `-0.0075` n `766`
- 1h: commodity avg `-0.0382` n `12`; crypto_alt avg `0.1259` n `230`; crypto_major avg `0.1478` n `8`; equity avg `0.1243` n `92`; fx avg `-0.0134` n `6`; index avg `0.0372` n `25`; metal avg `0.0901` n `20`; unknown avg `0.069` n `766`
- 4h: commodity avg `-0.0967` n `12`; crypto_alt avg `0.8624` n `230`; crypto_major avg `0.1187` n `8`; equity avg `-0.2607` n `92`; fx avg `-0.0427` n `6`; index avg `-0.0247` n `25`; metal avg `0.154` n `20`; unknown avg `0.0109` n `750`
- 24h: commodity avg `-0.0939` n `12`; crypto_alt avg `-1.0293` n `230`; crypto_major avg `-0.8418` n `8`; equity avg `-2.3102` n `92`; fx avg `-0.003` n `6`; index avg `-0.4816` n `25`; metal avg `-0.3227` n `20`; unknown avg `-0.0308` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
