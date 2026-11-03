# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T06:37:28.936985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `0.0758` n `239`; crypto_major avg `0.2514` n `8`; equity avg `0.3295` n `157`; fx avg `0.0062` n `6`; index avg `0.0306` n `27`; metal avg `0.0518` n `20`; unknown avg `0.3439` n `1260`
- 1h: commodity avg `0.0311` n `13`; crypto_alt avg `-0.0976` n `239`; crypto_major avg `0.1564` n `8`; equity avg `0.1404` n `157`; fx avg `0.0028` n `6`; index avg `0.0263` n `27`; metal avg `0.0182` n `20`; unknown avg `0.0102` n `1238`
- 4h: commodity avg `0.1653` n `13`; crypto_alt avg `-0.4954` n `239`; crypto_major avg `-0.3346` n `8`; equity avg `-0.927` n `157`; fx avg `0.0376` n `6`; index avg `-0.0927` n `27`; metal avg `-0.3025` n `20`; unknown avg `3.9623` n `1168`
- 24h: commodity avg `-0.7848` n `13`; crypto_alt avg `-2.5035` n `238`; crypto_major avg `-1.6189` n `8`; equity avg `-4.3091` n `157`; fx avg `0.007` n `6`; index avg `-0.3273` n `27`; metal avg `-0.3103` n `20`; unknown avg `8.1812` n `953`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
