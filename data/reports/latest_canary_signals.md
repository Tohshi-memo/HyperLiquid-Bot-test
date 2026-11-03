# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T05:52:27.284790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `13`; crypto_alt avg `0.0528` n `239`; crypto_major avg `0.0712` n `8`; equity avg `0.0531` n `157`; fx avg `0.0016` n `6`; index avg `0.0179` n `27`; metal avg `-0.0186` n `20`; unknown avg `-0.0641` n `1264`
- 1h: commodity avg `0.0067` n `13`; crypto_alt avg `-0.3051` n `239`; crypto_major avg `-0.2692` n `8`; equity avg `-0.2278` n `157`; fx avg `0.0331` n `6`; index avg `0.0059` n `27`; metal avg `-0.0876` n `20`; unknown avg `0.2076` n `1250`
- 4h: commodity avg `0.1774` n `13`; crypto_alt avg `-0.4964` n `239`; crypto_major avg `-0.5258` n `8`; equity avg `-1.0856` n `157`; fx avg `-0.0113` n `6`; index avg `-0.1223` n `27`; metal avg `-0.4281` n `20`; unknown avg `-0.3537` n `1188`
- 24h: commodity avg `-0.7806` n `13`; crypto_alt avg `-3.115` n `238`; crypto_major avg `-2.2199` n `8`; equity avg `-4.6382` n `157`; fx avg `0.0393` n `6`; index avg `-0.3827` n `27`; metal avg `-0.4515` n `20`; unknown avg `8.1389` n `955`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
