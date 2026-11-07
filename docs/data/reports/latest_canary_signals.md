# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T05:52:25.912003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `13`; crypto_alt avg `0.0875` n `239`; crypto_major avg `0.0746` n `8`; equity avg `-0.0116` n `158`; fx avg `-0.0182` n `6`; index avg `-0.0037` n `27`; metal avg `-0.0012` n `20`; unknown avg `0.7754` n `1261`
- 1h: commodity avg `0.0036` n `13`; crypto_alt avg `0.1412` n `239`; crypto_major avg `0.2795` n `8`; equity avg `-0.0804` n `158`; fx avg `-0.0219` n `6`; index avg `-0.0072` n `27`; metal avg `-0.0026` n `20`; unknown avg `46.322` n `1255`
- 4h: commodity avg `-0.0661` n `13`; crypto_alt avg `-0.2932` n `239`; crypto_major avg `-0.2929` n `8`; equity avg `-0.2005` n `158`; fx avg `-0.018` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0066` n `20`; unknown avg `-0.2348` n `1233`
- 24h: commodity avg `-0.2571` n `13`; crypto_alt avg `0.5835` n `239`; crypto_major avg `0.338` n `8`; equity avg `1.3147` n `158`; fx avg `-0.1068` n `6`; index avg `0.1598` n `27`; metal avg `0.2798` n `20`; unknown avg `8.4163` n `1010`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
