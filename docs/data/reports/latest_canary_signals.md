# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T05:07:31.773635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0506` n `12`; crypto_alt avg `0.0333` n `230`; crypto_major avg `0.0064` n `8`; equity avg `-0.0345` n `102`; fx avg `-0.0156` n `6`; index avg `0.0171` n `25`; metal avg `0.0003` n `20`; unknown avg `0.069` n `782`
- 1h: commodity avg `0.1473` n `12`; crypto_alt avg `0.1982` n `230`; crypto_major avg `0.0827` n `8`; equity avg `0.0028` n `102`; fx avg `-0.0072` n `6`; index avg `-0.0077` n `25`; metal avg `0.0226` n `20`; unknown avg `0.0479` n `782`
- 4h: commodity avg `-0.8417` n `12`; crypto_alt avg `0.7544` n `230`; crypto_major avg `1.0073` n `8`; equity avg `0.7139` n `102`; fx avg `-0.062` n `6`; index avg `0.205` n `25`; metal avg `0.1453` n `20`; unknown avg `1.2991` n `782`
- 24h: commodity avg `-1.0242` n `12`; crypto_alt avg `0.0445` n `230`; crypto_major avg `0.3182` n `8`; equity avg `0.8126` n `102`; fx avg `-0.1148` n `6`; index avg `0.2173` n `25`; metal avg `0.2577` n `20`; unknown avg `0.0144` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
