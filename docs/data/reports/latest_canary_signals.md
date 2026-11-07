# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T12:52:25.863350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0105` n `13`; crypto_alt avg `-0.0607` n `239`; crypto_major avg `-0.0786` n `8`; equity avg `0.0588` n `158`; fx avg `0.0001` n `6`; index avg `0.0029` n `27`; metal avg `-0.0068` n `20`; unknown avg `0.7521` n `1261`
- 1h: commodity avg `-0.0251` n `13`; crypto_alt avg `-0.2108` n `239`; crypto_major avg `-0.3074` n `8`; equity avg `0.0379` n `158`; fx avg `0.0378` n `6`; index avg `0.0045` n `27`; metal avg `-0.0037` n `20`; unknown avg `-0.0511` n `1249`
- 4h: commodity avg `0.0337` n `13`; crypto_alt avg `-0.6852` n `239`; crypto_major avg `-0.591` n `8`; equity avg `-0.0223` n `158`; fx avg `0.0538` n `6`; index avg `-0.014` n `27`; metal avg `-0.011` n `20`; unknown avg `132.3221` n `1233`
- 24h: commodity avg `0.078` n `13`; crypto_alt avg `-1.4297` n `239`; crypto_major avg `-0.6008` n `8`; equity avg `-0.4881` n `158`; fx avg `0.0023` n `6`; index avg `-0.0076` n `27`; metal avg `0.0417` n `20`; unknown avg `-0.5287` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
