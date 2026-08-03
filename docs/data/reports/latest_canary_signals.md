# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T21:52:35.356183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `0.0268` n `230`; crypto_major avg `-0.0762` n `8`; equity avg `0.0566` n `103`; fx avg `-0.0037` n `6`; index avg `0.0017` n `25`; metal avg `-0.0017` n `20`; unknown avg `1.8772` n `784`
- 1h: commodity avg `0.0217` n `12`; crypto_alt avg `0.1631` n `230`; crypto_major avg `-0.1354` n `8`; equity avg `0.1446` n `103`; fx avg `0.0012` n `6`; index avg `-0.008` n `25`; metal avg `-0.0062` n `20`; unknown avg `2.9111` n `784`
- 4h: commodity avg `0.0301` n `12`; crypto_alt avg `0.2597` n `230`; crypto_major avg `-0.2467` n `8`; equity avg `0.3896` n `103`; fx avg `0.0229` n `6`; index avg `0.0603` n `25`; metal avg `0.203` n `20`; unknown avg `2.2197` n `784`
- 24h: commodity avg `0.0799` n `12`; crypto_alt avg `0.1791` n `230`; crypto_major avg `-0.0913` n `8`; equity avg `1.9647` n `103`; fx avg `-0.3042` n `6`; index avg `0.0685` n `25`; metal avg `-0.4405` n `20`; unknown avg `-0.0128` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
