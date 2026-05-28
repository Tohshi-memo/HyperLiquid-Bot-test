# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T23:07:18.165493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.032` n `12`; crypto_alt avg `0.026` n `228`; crypto_major avg `0.0615` n `8`; equity avg `-0.0036` n `69`; fx avg `0.0026` n `6`; index avg `0.0259` n `23`; metal avg `0.0271` n `18`; unknown avg `-0.1877` n `417`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `-0.416` n `228`; crypto_major avg `-0.2281` n `8`; equity avg `0.0956` n `69`; fx avg `0.0016` n `6`; index avg `-0.0149` n `23`; metal avg `-0.0668` n `18`; unknown avg `-0.3658` n `417`
- 4h: commodity avg `-0.154` n `12`; crypto_alt avg `-0.4371` n `228`; crypto_major avg `-0.0923` n `8`; equity avg `0.5008` n `69`; fx avg `-0.0045` n `6`; index avg `-0.1666` n `23`; metal avg `-0.028` n `18`; unknown avg `-0.2386` n `417`
- 24h: commodity avg `0.8349` n `12`; crypto_alt avg `-1.9846` n `228`; crypto_major avg `0.2351` n `8`; equity avg `2.2447` n `69`; fx avg `-0.0151` n `6`; index avg `0.7838` n `23`; metal avg `0.5278` n `18`; unknown avg `-0.1824` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
