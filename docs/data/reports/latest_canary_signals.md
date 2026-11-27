# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T09:22:27.633749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0592` n `13`; crypto_alt avg `-0.0408` n `239`; crypto_major avg `-0.1361` n `8`; equity avg `0.1215` n `168`; fx avg `-0.0226` n `6`; index avg `-0.0091` n `27`; metal avg `-0.0302` n `20`; unknown avg `-0.0718` n `1261`
- 1h: commodity avg `-0.1666` n `13`; crypto_alt avg `-0.1115` n `239`; crypto_major avg `-0.3606` n `8`; equity avg `0.3695` n `168`; fx avg `0.0028` n `6`; index avg `0.0298` n `27`; metal avg `0.0176` n `20`; unknown avg `0.8926` n `1163`
- 4h: commodity avg `-0.3659` n `13`; crypto_alt avg `0.159` n `239`; crypto_major avg `-0.0133` n `8`; equity avg `0.5467` n `168`; fx avg `-0.0948` n `6`; index avg `0.0067` n `27`; metal avg `0.3074` n `20`; unknown avg `1.4923` n `1101`
- 24h: commodity avg `0.3587` n `13`; crypto_alt avg `1.9445` n `239`; crypto_major avg `2.5941` n `8`; equity avg `4.5045` n `168`; fx avg `-0.1124` n `6`; index avg `0.3733` n `27`; metal avg `1.2636` n `20`; unknown avg `188.523` n `1025`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
