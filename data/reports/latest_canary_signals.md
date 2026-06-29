# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T06:52:31.665665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0611` n `12`; crypto_alt avg `-0.0107` n `228`; crypto_major avg `0.0261` n `8`; equity avg `0.037` n `88`; fx avg `-0.0225` n `6`; index avg `-0.0162` n `23`; metal avg `0.0387` n `20`; unknown avg `-0.0427` n `764`
- 1h: commodity avg `0.1209` n `12`; crypto_alt avg `0.3985` n `228`; crypto_major avg `0.3806` n `8`; equity avg `0.2631` n `88`; fx avg `0.04` n `6`; index avg `-0.0157` n `23`; metal avg `0.1528` n `20`; unknown avg `0.2196` n `732`
- 4h: commodity avg `0.0112` n `12`; crypto_alt avg `0.4077` n `228`; crypto_major avg `0.3013` n `8`; equity avg `0.6801` n `88`; fx avg `0.0116` n `6`; index avg `0.1402` n `23`; metal avg `0.0108` n `20`; unknown avg `0.2363` n `732`
- 24h: commodity avg `-0.3363` n `12`; crypto_alt avg `0.707` n `228`; crypto_major avg `0.5339` n `8`; equity avg `0.5757` n `88`; fx avg `0.0607` n `6`; index avg `0.1032` n `23`; metal avg `-0.0971` n `20`; unknown avg `-0.3655` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
