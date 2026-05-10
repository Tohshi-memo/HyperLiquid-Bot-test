# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T02:52:12.635135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0256` n `228`; crypto_major avg `-0.0767` n `8`; equity avg `0.0179` n `65`; fx avg `0.0` n `5`; index avg `-0.0083` n `23`; metal avg `0.0072` n `18`; unknown avg `-0.0643` n `376`
- 1h: commodity avg `-0.0185` n `12`; crypto_alt avg `0.3978` n `228`; crypto_major avg `0.12` n `8`; equity avg `0.0958` n `65`; fx avg `0.0` n `5`; index avg `0.036` n `23`; metal avg `0.032` n `18`; unknown avg `0.2747` n `376`
- 4h: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.6764` n `228`; crypto_major avg `-0.3801` n `8`; equity avg `0.0884` n `65`; fx avg `0.0002` n `5`; index avg `0.1128` n `23`; metal avg `0.0372` n `18`; unknown avg `0.0113` n `376`
- 24h: commodity avg `0.3612` n `12`; crypto_alt avg `-1.5945` n `228`; crypto_major avg `-0.771` n `8`; equity avg `0.6956` n `65`; fx avg `-0.0098` n `5`; index avg `0.2922` n `23`; metal avg `0.0951` n `18`; unknown avg `-0.6329` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
