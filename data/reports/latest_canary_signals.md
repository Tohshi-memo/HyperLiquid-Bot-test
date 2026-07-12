# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T13:07:53.886588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0351` n `12`; crypto_alt avg `0.088` n `230`; crypto_major avg `0.1715` n `8`; equity avg `0.0148` n `92`; fx avg `0.0022` n `6`; index avg `-0.0058` n `25`; metal avg `0.0062` n `20`; unknown avg `-0.0425` n `765`
- 1h: commodity avg `-0.0187` n `12`; crypto_alt avg `0.0487` n `230`; crypto_major avg `0.2855` n `8`; equity avg `0.0114` n `92`; fx avg `-0.0005` n `6`; index avg `-0.0088` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0505` n `765`
- 4h: commodity avg `-0.0315` n `12`; crypto_alt avg `0.0934` n `230`; crypto_major avg `0.4291` n `8`; equity avg `0.0475` n `92`; fx avg `0.0007` n `6`; index avg `-0.0145` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.2397` n `763`
- 24h: commodity avg `0.4175` n `12`; crypto_alt avg `-0.9129` n `230`; crypto_major avg `-0.2946` n `8`; equity avg `-0.0178` n `92`; fx avg `0.0124` n `6`; index avg `-0.1192` n `25`; metal avg `-0.097` n `20`; unknown avg `0.1127` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
