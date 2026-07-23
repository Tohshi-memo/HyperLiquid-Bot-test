# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T12:07:31.153392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.0016` n `230`; crypto_major avg `-0.0709` n `8`; equity avg `-0.1341` n `99`; fx avg `0.0057` n `6`; index avg `0.0029` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0168` n `772`
- 1h: commodity avg `-0.0022` n `12`; crypto_alt avg `0.0478` n `230`; crypto_major avg `-0.0796` n `8`; equity avg `-0.4867` n `99`; fx avg `0.0151` n `6`; index avg `-0.0988` n `25`; metal avg `-0.0431` n `20`; unknown avg `0.0193` n `772`
- 4h: commodity avg `0.185` n `12`; crypto_alt avg `0.1319` n `230`; crypto_major avg `0.2018` n `8`; equity avg `-0.2892` n `99`; fx avg `-0.0167` n `6`; index avg `-0.0657` n `25`; metal avg `-0.1428` n `20`; unknown avg `0.0057` n `772`
- 24h: commodity avg `0.6934` n `12`; crypto_alt avg `-0.1648` n `230`; crypto_major avg `0.0917` n `8`; equity avg `0.5351` n `99`; fx avg `-0.081` n `6`; index avg `0.1445` n `25`; metal avg `-0.4869` n `20`; unknown avg `10.1876` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0727`, n `666`, weak_sample_signal
