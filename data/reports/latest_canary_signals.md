# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T06:52:35.736110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1443` n `13`; crypto_alt avg `-0.3763` n `239`; crypto_major avg `-0.3396` n `8`; equity avg `-0.1664` n `157`; fx avg `-0.0189` n `6`; index avg `-0.0187` n `27`; metal avg `-0.102` n `20`; unknown avg `0.5085` n `1264`
- 1h: commodity avg `0.1907` n `13`; crypto_alt avg `-0.5259` n `239`; crypto_major avg `-0.2547` n `8`; equity avg `-0.0795` n `157`; fx avg `-0.0177` n `6`; index avg `-0.0103` n `27`; metal avg `-0.0654` n `20`; unknown avg `4.2488` n `1238`
- 4h: commodity avg `0.3459` n `13`; crypto_alt avg `-0.4885` n `239`; crypto_major avg `-0.3744` n `8`; equity avg `-0.9397` n `157`; fx avg `0.0204` n `6`; index avg `-0.0839` n `27`; metal avg `-0.4216` n `20`; unknown avg `0.3465` n `1168`
- 24h: commodity avg `-0.6176` n `13`; crypto_alt avg `-2.8507` n `238`; crypto_major avg `-1.9101` n `8`; equity avg `-4.47` n `157`; fx avg `-0.0273` n `6`; index avg `-0.3481` n `27`; metal avg `-0.4296` n `20`; unknown avg `8.665` n `953`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
