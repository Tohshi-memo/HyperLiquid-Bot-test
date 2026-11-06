# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T10:22:24.876994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.05` n `13`; crypto_alt avg `0.1481` n `239`; crypto_major avg `0.0502` n `8`; equity avg `0.0566` n `158`; fx avg `0.005` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0556` n `20`; unknown avg `0.0037` n `1256`
- 1h: commodity avg `0.0794` n `13`; crypto_alt avg `0.2469` n `239`; crypto_major avg `-0.1098` n `8`; equity avg `-0.1586` n `158`; fx avg `-0.0024` n `6`; index avg `-0.0067` n `27`; metal avg `-0.1721` n `20`; unknown avg `-0.1504` n `1252`
- 4h: commodity avg `-0.3051` n `13`; crypto_alt avg `1.0759` n `239`; crypto_major avg `0.579` n `8`; equity avg `1.703` n `158`; fx avg `-0.0969` n `6`; index avg `0.2221` n `27`; metal avg `0.13` n `20`; unknown avg `15.8436` n `1188`
- 24h: commodity avg `0.6318` n `13`; crypto_alt avg `-3.4207` n `239`; crypto_major avg `-5.504` n `8`; equity avg `-4.9352` n `158`; fx avg `-0.0436` n `6`; index avg `-0.6524` n `27`; metal avg `-0.343` n `20`; unknown avg `226.7952` n `1075`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2227`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
