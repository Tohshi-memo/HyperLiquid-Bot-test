# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T12:22:47.837451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0328` n `13`; crypto_alt avg `0.2055` n `238`; crypto_major avg `0.1138` n `8`; equity avg `0.1852` n `156`; fx avg `0.0059` n `6`; index avg `0.0115` n `27`; metal avg `0.0379` n `20`; unknown avg `-0.1514` n `1265`
- 1h: commodity avg `0.0962` n `13`; crypto_alt avg `0.3763` n `238`; crypto_major avg `0.2898` n `8`; equity avg `0.0017` n `156`; fx avg `0.0124` n `6`; index avg `-0.0121` n `27`; metal avg `-0.0243` n `20`; unknown avg `0.1281` n `1252`
- 4h: commodity avg `-0.038` n `13`; crypto_alt avg `0.1697` n `238`; crypto_major avg `0.0661` n `8`; equity avg `0.125` n `156`; fx avg `0.0292` n `6`; index avg `0.0224` n `27`; metal avg `-0.0321` n `20`; unknown avg `3.0931` n `1250`
- 24h: commodity avg `-0.5157` n `13`; crypto_alt avg `-1.4019` n `238`; crypto_major avg `-0.0913` n `8`; equity avg `0.9463` n `156`; fx avg `0.2912` n `6`; index avg `0.2876` n `27`; metal avg `0.047` n `20`; unknown avg `3.5348` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
