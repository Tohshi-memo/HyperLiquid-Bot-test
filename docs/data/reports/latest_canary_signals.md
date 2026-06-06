# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T11:07:23.188069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1547` n `12`; crypto_alt avg `0.7654` n `228`; crypto_major avg `0.6581` n `8`; equity avg `0.2529` n `74`; fx avg `0.0059` n `6`; index avg `0.0801` n `23`; metal avg `0.0498` n `18`; unknown avg `0.3191` n `425`
- 1h: commodity avg `0.1456` n `12`; crypto_alt avg `0.5061` n `228`; crypto_major avg `0.1794` n `8`; equity avg `0.1325` n `74`; fx avg `-0.0002` n `6`; index avg `0.1042` n `23`; metal avg `0.001` n `18`; unknown avg `1.0226` n `425`
- 4h: commodity avg `0.2101` n `12`; crypto_alt avg `0.3738` n `228`; crypto_major avg `-0.2198` n `8`; equity avg `-0.0089` n `74`; fx avg `0.0114` n `6`; index avg `0.1976` n `23`; metal avg `-0.0223` n `18`; unknown avg `0.1288` n `425`
- 24h: commodity avg `-1.133` n `12`; crypto_alt avg `-3.7878` n `228`; crypto_major avg `-3.9416` n `8`; equity avg `-6.8956` n `74`; fx avg `-0.2631` n `6`; index avg `-4.0577` n `23`; metal avg `-4.3697` n `18`; unknown avg `1.7684` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
