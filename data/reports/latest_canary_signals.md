# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T19:22:35.051745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `-0.0617` n `229`; crypto_major avg `-0.0849` n `8`; equity avg `-0.0855` n `92`; fx avg `-0.0015` n `6`; index avg `-0.0204` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.0695` n `765`
- 1h: commodity avg `0.0874` n `12`; crypto_alt avg `-0.2754` n `229`; crypto_major avg `-0.337` n `8`; equity avg `-0.0929` n `92`; fx avg `-0.0031` n `6`; index avg `-0.0023` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0669` n `765`
- 4h: commodity avg `0.1512` n `12`; crypto_alt avg `-0.2173` n `229`; crypto_major avg `-0.3149` n `8`; equity avg `0.1871` n `92`; fx avg `-0.0413` n `6`; index avg `0.0484` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.1323` n `765`
- 24h: commodity avg `-0.157` n `12`; crypto_alt avg `0.3936` n `229`; crypto_major avg `0.661` n `8`; equity avg `-0.8039` n `92`; fx avg `-0.1586` n `6`; index avg `0.0244` n `25`; metal avg `0.0684` n `20`; unknown avg `-0.1623` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
