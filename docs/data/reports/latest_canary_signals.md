# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T13:52:29.404532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `13`; crypto_alt avg `0.1612` n `239`; crypto_major avg `0.0021` n `8`; equity avg `0.1994` n `156`; fx avg `-0.0053` n `6`; index avg `-0.0078` n `27`; metal avg `0.0877` n `20`; unknown avg `-0.0217` n `1263`
- 1h: commodity avg `-0.3471` n `13`; crypto_alt avg `0.448` n `238`; crypto_major avg `0.2819` n `8`; equity avg `0.1128` n `156`; fx avg `-0.0078` n `6`; index avg `0.043` n `27`; metal avg `0.2258` n `20`; unknown avg `203.1782` n `1257`
- 4h: commodity avg `-0.2518` n `13`; crypto_alt avg `0.2874` n `238`; crypto_major avg `-0.0349` n `8`; equity avg `-0.4416` n `156`; fx avg `-0.006` n `6`; index avg `0.0054` n `27`; metal avg `0.167` n `20`; unknown avg `3.8039` n `1250`
- 24h: commodity avg `-0.8085` n `13`; crypto_alt avg `-1.9815` n `238`; crypto_major avg `-0.3914` n `8`; equity avg `0.5416` n `156`; fx avg `0.2898` n `6`; index avg `0.2778` n `27`; metal avg `0.1927` n `20`; unknown avg `6.9888` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1906`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
