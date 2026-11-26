# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T12:37:27.048086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `13`; crypto_alt avg `0.0484` n `239`; crypto_major avg `0.2339` n `8`; equity avg `0.0867` n `168`; fx avg `0.009` n `6`; index avg `0.0018` n `27`; metal avg `0.077` n `20`; unknown avg `-0.0639` n `1267`
- 1h: commodity avg `-0.1048` n `13`; crypto_alt avg `0.0376` n `239`; crypto_major avg `0.1538` n `8`; equity avg `0.2598` n `168`; fx avg `0.0117` n `6`; index avg `0.0321` n `27`; metal avg `0.0608` n `20`; unknown avg `0.889` n `1255`
- 4h: commodity avg `0.0601` n `13`; crypto_alt avg `0.2914` n `239`; crypto_major avg `-0.0419` n `8`; equity avg `0.372` n `168`; fx avg `0.0294` n `6`; index avg `0.0281` n `27`; metal avg `0.04` n `20`; unknown avg `163.0568` n `1251`
- 24h: commodity avg `0.3204` n `13`; crypto_alt avg `4.4541` n `239`; crypto_major avg `3.6071` n `8`; equity avg `4.3244` n `168`; fx avg `0.071` n `6`; index avg `0.4153` n `27`; metal avg `0.6818` n `20`; unknown avg `1.258` n `1053`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
