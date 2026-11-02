# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T06:22:25.813097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `-0.3813` n `238`; crypto_major avg `-0.249` n `8`; equity avg `-0.1933` n `156`; fx avg `0.0147` n `6`; index avg `-0.0288` n `27`; metal avg `-0.0185` n `20`; unknown avg `3.5567` n `1264`
- 1h: commodity avg `0.1201` n `13`; crypto_alt avg `-0.6216` n `238`; crypto_major avg `-0.2488` n `8`; equity avg `-0.0216` n `156`; fx avg `0.0044` n `6`; index avg `-0.0692` n `27`; metal avg `0.0391` n `20`; unknown avg `1.3907` n `1235`
- 4h: commodity avg `-0.1182` n `13`; crypto_alt avg `-0.881` n `238`; crypto_major avg `-0.4001` n `8`; equity avg `0.3494` n `156`; fx avg `0.0395` n `6`; index avg `0.0649` n `27`; metal avg `0.0213` n `20`; unknown avg `1.0683` n `1179`
- 24h: commodity avg `-0.3669` n `13`; crypto_alt avg `-1.7443` n `238`; crypto_major avg `-0.1193` n `8`; equity avg `1.1104` n `156`; fx avg `0.1845` n `6`; index avg `0.3237` n `27`; metal avg `0.1601` n `20`; unknown avg `2.8876` n `1069`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
