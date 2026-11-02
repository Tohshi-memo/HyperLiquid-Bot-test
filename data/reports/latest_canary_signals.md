# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T12:07:29.306767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0636` n `13`; crypto_alt avg `0.1903` n `238`; crypto_major avg `0.1921` n `8`; equity avg `-0.0775` n `156`; fx avg `0.0025` n `6`; index avg `-0.012` n `27`; metal avg `-0.0192` n `20`; unknown avg `0.2252` n `1253`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `0.1578` n `238`; crypto_major avg `0.1347` n `8`; equity avg `-0.1874` n `156`; fx avg `0.016` n `6`; index avg `-0.0206` n `27`; metal avg `-0.0642` n `20`; unknown avg `0.421` n `1252`
- 4h: commodity avg `-0.0635` n `13`; crypto_alt avg `-0.2247` n `238`; crypto_major avg `-0.1432` n `8`; equity avg `-0.1532` n `156`; fx avg `0.0398` n `6`; index avg `-0.0246` n `27`; metal avg `-0.1` n `20`; unknown avg `3.7163` n `1250`
- 24h: commodity avg `-0.5307` n `13`; crypto_alt avg `-1.9651` n `238`; crypto_major avg `-0.5997` n `8`; equity avg `0.6476` n `156`; fx avg `0.2868` n `6`; index avg `0.2664` n `27`; metal avg `-0.0082` n `20`; unknown avg `3.987` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
