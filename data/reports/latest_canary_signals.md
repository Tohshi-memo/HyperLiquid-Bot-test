# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T12:52:30.430191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `13`; crypto_alt avg `-0.0923` n `238`; crypto_major avg `-0.1039` n `8`; equity avg `-0.0433` n `156`; fx avg `0.001` n `6`; index avg `-0.0017` n `27`; metal avg `0.0122` n `20`; unknown avg `0.353` n `1265`
- 1h: commodity avg `0.1343` n `13`; crypto_alt avg `-0.0533` n `238`; crypto_major avg `-0.0579` n `8`; equity avg `-0.3286` n `156`; fx avg `0.011` n `6`; index avg `-0.024` n `27`; metal avg `-0.047` n `20`; unknown avg `0.0804` n `1253`
- 4h: commodity avg `0.0647` n `13`; crypto_alt avg `-0.4188` n `238`; crypto_major avg `-0.6106` n `8`; equity avg `-0.4447` n `156`; fx avg `0.0054` n `6`; index avg `-0.0261` n `27`; metal avg `-0.1878` n `20`; unknown avg `2.9932` n `1250`
- 24h: commodity avg `-0.46` n `13`; crypto_alt avg `-2.1834` n `238`; crypto_major avg `-0.6328` n `8`; equity avg `0.4625` n `156`; fx avg `0.2928` n `6`; index avg `0.2595` n `27`; metal avg `-0.029` n `20`; unknown avg `3.4586` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
