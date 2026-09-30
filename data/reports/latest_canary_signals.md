# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T03:22:29.567715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `-0.1176` n `234`; crypto_major avg `-0.1859` n `8`; equity avg `-0.0391` n `142`; fx avg `-0.0047` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0134` n `20`; unknown avg `2.0016` n `963`
- 1h: commodity avg `0.0897` n `12`; crypto_alt avg `-0.1378` n `234`; crypto_major avg `-0.1439` n `8`; equity avg `-0.0484` n `142`; fx avg `0.0394` n `6`; index avg `-0.0163` n `26`; metal avg `0.0245` n `20`; unknown avg `1.4953` n `961`
- 4h: commodity avg `0.08` n `12`; crypto_alt avg `-0.2765` n `234`; crypto_major avg `-0.2957` n `8`; equity avg `-0.3028` n `142`; fx avg `-0.0401` n `6`; index avg `-0.0568` n `26`; metal avg `-0.0846` n `20`; unknown avg `4.5245` n `955`
- 24h: commodity avg `-0.9101` n `12`; crypto_alt avg `1.7997` n `234`; crypto_major avg `0.3779` n `8`; equity avg `0.9454` n `142`; fx avg `-0.1735` n `6`; index avg `0.1157` n `26`; metal avg `0.1883` n `20`; unknown avg `3242.9481` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
