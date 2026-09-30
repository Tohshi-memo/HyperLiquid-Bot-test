# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T07:52:37.600751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `12`; crypto_alt avg `0.1405` n `234`; crypto_major avg `0.1187` n `8`; equity avg `0.0552` n `142`; fx avg `-0.0095` n `6`; index avg `0.008` n `26`; metal avg `-0.0165` n `20`; unknown avg `7.6548` n `963`
- 1h: commodity avg `-0.15` n `12`; crypto_alt avg `0.779` n `234`; crypto_major avg `0.5592` n `8`; equity avg `0.3412` n `142`; fx avg `-0.0349` n `6`; index avg `0.0719` n `26`; metal avg `0.0942` n `20`; unknown avg `9.5084` n `959`
- 4h: commodity avg `-0.1409` n `12`; crypto_alt avg `0.7894` n `234`; crypto_major avg `0.2784` n `8`; equity avg `0.2544` n `142`; fx avg `0.0079` n `6`; index avg `0.0699` n `26`; metal avg `0.2129` n `20`; unknown avg `6.0179` n `925`
- 24h: commodity avg `-0.8607` n `12`; crypto_alt avg `-0.0041` n `234`; crypto_major avg `-0.9061` n `8`; equity avg `0.5415` n `142`; fx avg `-0.1027` n `6`; index avg `0.1201` n `26`; metal avg `0.3706` n `20`; unknown avg `2892.2236` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
