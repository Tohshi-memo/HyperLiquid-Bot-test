# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T04:22:29.211296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.1013` n `230`; crypto_major avg `-0.0444` n `8`; equity avg `-0.0082` n `93`; fx avg `0.0068` n `6`; index avg `-0.0144` n `25`; metal avg `0.0268` n `20`; unknown avg `0.1341` n `767`
- 1h: commodity avg `-0.0595` n `12`; crypto_alt avg `0.062` n `230`; crypto_major avg `0.0947` n `8`; equity avg `0.3011` n `93`; fx avg `0.0249` n `6`; index avg `0.0337` n `25`; metal avg `0.0242` n `20`; unknown avg `0.1418` n `767`
- 4h: commodity avg `-0.079` n `12`; crypto_alt avg `-0.0241` n `230`; crypto_major avg `0.1035` n `8`; equity avg `1.0287` n `93`; fx avg `0.045` n `6`; index avg `0.0696` n `25`; metal avg `-0.0868` n `20`; unknown avg `-0.1927` n `767`
- 24h: commodity avg `0.1134` n `12`; crypto_alt avg `1.8401` n `230`; crypto_major avg `3.2606` n `8`; equity avg `2.8665` n `92`; fx avg `0.1579` n `6`; index avg `0.7772` n `25`; metal avg `0.4099` n `20`; unknown avg `0.3203` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0441`, n `668`, weak_sample_signal
