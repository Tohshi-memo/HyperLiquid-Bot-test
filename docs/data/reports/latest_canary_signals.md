# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T16:22:31.206850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `12`; crypto_alt avg `-0.1042` n `230`; crypto_major avg `-0.0386` n `8`; equity avg `-0.0028` n `100`; fx avg `-0.0001` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0244` n `774`
- 1h: commodity avg `0.0261` n `12`; crypto_alt avg `0.0162` n `230`; crypto_major avg `0.0424` n `8`; equity avg `-0.0197` n `100`; fx avg `-0.0016` n `6`; index avg `0.0059` n `25`; metal avg `-0.0185` n `20`; unknown avg `0.0393` n `774`
- 4h: commodity avg `-0.3476` n `12`; crypto_alt avg `0.5351` n `230`; crypto_major avg `0.683` n `8`; equity avg `-0.0148` n `100`; fx avg `-0.0017` n `6`; index avg `0.0104` n `25`; metal avg `0.0117` n `20`; unknown avg `0.0072` n `774`
- 24h: commodity avg `-0.3035` n `12`; crypto_alt avg `0.0081` n `230`; crypto_major avg `0.4102` n `8`; equity avg `-1.5431` n `100`; fx avg `-0.0386` n `6`; index avg `-0.2181` n `25`; metal avg `-0.2401` n `20`; unknown avg `-0.3225` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1255`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1151`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1096`, n `666`, weak_sample_signal
