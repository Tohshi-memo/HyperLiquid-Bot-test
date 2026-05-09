# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T09:22:18.256396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.4624` n `228`; crypto_major avg `-0.163` n `8`; equity avg `-0.0325` n `65`; fx avg `0.0` n `5`; index avg `0.0157` n `23`; metal avg `-0.0095` n `18`; unknown avg `-0.1679` n `376`
- 1h: commodity avg `0.0352` n `12`; crypto_alt avg `-0.658` n `228`; crypto_major avg `-0.1689` n `8`; equity avg `-0.0857` n `65`; fx avg `-0.0008` n `5`; index avg `0.052` n `23`; metal avg `-0.0019` n `18`; unknown avg `-0.1828` n `376`
- 4h: commodity avg `0.038` n `12`; crypto_alt avg `-0.8514` n `228`; crypto_major avg `-0.2738` n `8`; equity avg `0.0433` n `65`; fx avg `0.0202` n `5`; index avg `0.0981` n `23`; metal avg `0.0004` n `18`; unknown avg `-0.3988` n `356`
- 24h: commodity avg `0.1353` n `12`; crypto_alt avg `2.8918` n `228`; crypto_major avg `1.9865` n `8`; equity avg `2.5648` n `65`; fx avg `-0.0148` n `5`; index avg `1.1718` n `23`; metal avg `-0.2021` n `18`; unknown avg `0.2956` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
