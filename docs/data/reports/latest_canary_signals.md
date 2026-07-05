# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T07:52:30.243486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `0.1431` n `229`; crypto_major avg `0.1036` n `8`; equity avg `0.0222` n `88`; fx avg `-0.0022` n `6`; index avg `0.0018` n `25`; metal avg `0.0126` n `20`; unknown avg `0.0167` n `765`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.2385` n `229`; crypto_major avg `0.2052` n `8`; equity avg `0.0484` n `88`; fx avg `-0.0007` n `6`; index avg `0.0005` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0347` n `765`
- 4h: commodity avg `0.0105` n `12`; crypto_alt avg `0.1006` n `229`; crypto_major avg `0.2285` n `8`; equity avg `0.117` n `88`; fx avg `0.0088` n `6`; index avg `0.0247` n `25`; metal avg `0.0108` n `20`; unknown avg `-0.0132` n `731`
- 24h: commodity avg `0.0738` n `12`; crypto_alt avg `-0.4415` n `229`; crypto_major avg `-0.6651` n `8`; equity avg `0.2399` n `88`; fx avg `0.0149` n `6`; index avg `0.0735` n `25`; metal avg `0.076` n `20`; unknown avg `-1.1534` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
