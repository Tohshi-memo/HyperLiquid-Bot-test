# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T03:52:26.997667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.18` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0567` n `12`; crypto_alt avg `0.083` n `228`; crypto_major avg `-0.0022` n `8`; equity avg `0.0586` n `69`; fx avg `0.004` n `6`; index avg `-0.0398` n `23`; metal avg `-0.0293` n `18`; unknown avg `-0.2296` n `422`
- 1h: commodity avg `-0.2355` n `12`; crypto_alt avg `0.8711` n `228`; crypto_major avg `0.4501` n `8`; equity avg `0.1817` n `69`; fx avg `0.0232` n `6`; index avg `-0.1087` n `23`; metal avg `0.2305` n `18`; unknown avg `0.9099` n `422`
- 4h: commodity avg `-0.3311` n `12`; crypto_alt avg `0.0507` n `228`; crypto_major avg `-0.0791` n `8`; equity avg `-0.2556` n `69`; fx avg `0.0719` n `6`; index avg `-0.5306` n `23`; metal avg `0.2153` n `18`; unknown avg `-0.1157` n `422`
- 24h: commodity avg `-0.5877` n `12`; crypto_alt avg `-0.8281` n `228`; crypto_major avg `-1.1968` n `8`; equity avg `-0.6248` n `69`; fx avg `0.0254` n `6`; index avg `-0.9611` n `23`; metal avg `0.1316` n `18`; unknown avg `1.3202` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
