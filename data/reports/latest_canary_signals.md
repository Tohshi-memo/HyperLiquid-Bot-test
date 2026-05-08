# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T23:22:22.986395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `12`; crypto_alt avg `0.0527` n `228`; crypto_major avg `-0.0196` n `8`; equity avg `0.0323` n `65`; fx avg `0.0017` n `5`; index avg `-0.0331` n `23`; metal avg `-0.0092` n `18`; unknown avg `-0.0856` n `375`
- 1h: commodity avg `0.074` n `12`; crypto_alt avg `-0.0458` n `228`; crypto_major avg `-0.168` n `8`; equity avg `-0.0521` n `65`; fx avg `-0.0038` n `5`; index avg `-0.0181` n `23`; metal avg `-0.1928` n `18`; unknown avg `-0.251` n `375`
- 4h: commodity avg `-0.3304` n `12`; crypto_alt avg `0.4255` n `228`; crypto_major avg `-0.1186` n `8`; equity avg `0.6758` n `65`; fx avg `-0.0112` n `5`; index avg `0.1008` n `23`; metal avg `-0.2877` n `18`; unknown avg `-0.4731` n `375`
- 24h: commodity avg `-0.7081` n `12`; crypto_alt avg `3.6544` n `228`; crypto_major avg `1.6455` n `8`; equity avg `4.1197` n `65`; fx avg `0.2166` n `5`; index avg `1.5823` n `23`; metal avg `0.7721` n `18`; unknown avg `0.8293` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
