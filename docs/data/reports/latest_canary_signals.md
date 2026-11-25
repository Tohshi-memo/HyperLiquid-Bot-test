# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T03:37:27.458725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `13`; crypto_alt avg `-0.0689` n `239`; crypto_major avg `-0.1066` n `8`; equity avg `0.2484` n `168`; fx avg `-0.0037` n `6`; index avg `0.0234` n `27`; metal avg `-0.0557` n `20`; unknown avg `157.7784` n `1265`
- 1h: commodity avg `-0.0678` n `13`; crypto_alt avg `0.4247` n `239`; crypto_major avg `0.4771` n `8`; equity avg `0.2675` n `168`; fx avg `0.007` n `6`; index avg `0.0606` n `27`; metal avg `-0.2046` n `20`; unknown avg `0.0315` n `1261`
- 4h: commodity avg `-0.26` n `13`; crypto_alt avg `-0.101` n `239`; crypto_major avg `-0.6085` n `8`; equity avg `-0.9272` n `168`; fx avg `0.0073` n `6`; index avg `-0.0963` n `27`; metal avg `-0.1332` n `20`; unknown avg `82.9225` n `1227`
- 24h: commodity avg `0.4244` n `13`; crypto_alt avg `-2.4783` n `239`; crypto_major avg `-2.2088` n `8`; equity avg `-4.7276` n `167`; fx avg `0.1878` n `6`; index avg `-0.4622` n `27`; metal avg `-0.9399` n `20`; unknown avg `498.284` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
