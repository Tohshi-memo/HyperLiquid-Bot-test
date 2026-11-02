# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T11:22:31.346241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0467` n `13`; crypto_alt avg `-0.0121` n `238`; crypto_major avg `-0.0409` n `8`; equity avg `-0.0054` n `156`; fx avg `0.0095` n `6`; index avg `0.0029` n `27`; metal avg `-0.0021` n `20`; unknown avg `0.5226` n `1264`
- 1h: commodity avg `-0.1316` n `13`; crypto_alt avg `0.0736` n `238`; crypto_major avg `-0.0602` n `8`; equity avg `-0.1` n `156`; fx avg `-0.0093` n `6`; index avg `0.001` n `27`; metal avg `0.0332` n `20`; unknown avg `1.4946` n `1258`
- 4h: commodity avg `-0.1985` n `13`; crypto_alt avg `-0.3479` n `238`; crypto_major avg `-0.1567` n `8`; equity avg `0.0232` n `156`; fx avg `0.0254` n `6`; index avg `0.0091` n `27`; metal avg `-0.087` n `20`; unknown avg `7.3689` n `1170`
- 24h: commodity avg `-0.5752` n `13`; crypto_alt avg `-2.1707` n `238`; crypto_major avg `-0.7225` n `8`; equity avg `0.8876` n `156`; fx avg `0.2692` n `6`; index avg `0.2957` n `27`; metal avg `0.0577` n `20`; unknown avg `3.7481` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
