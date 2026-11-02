# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T22:52:29.780215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `13`; crypto_alt avg `0.1991` n `239`; crypto_major avg `0.2334` n `8`; equity avg `0.2645` n `157`; fx avg `-0.0007` n `6`; index avg `0.0259` n `27`; metal avg `0.011` n `20`; unknown avg `9.8366` n `1264`
- 1h: commodity avg `0.049` n `13`; crypto_alt avg `-0.2121` n `239`; crypto_major avg `-0.0807` n `8`; equity avg `-0.1156` n `157`; fx avg `-0.0122` n `6`; index avg `-0.0278` n `27`; metal avg `0.0075` n `20`; unknown avg `0.6741` n `1258`
- 4h: commodity avg `0.012` n `13`; crypto_alt avg `0.2346` n `239`; crypto_major avg `0.3193` n `8`; equity avg `-0.95` n `157`; fx avg `0.0015` n `6`; index avg `-0.1716` n `27`; metal avg `-0.0318` n `20`; unknown avg `227.9103` n `1144`
- 24h: commodity avg `-1.3892` n `13`; crypto_alt avg `-2.3692` n `238`; crypto_major avg `-1.1066` n `8`; equity avg `-2.8833` n `157`; fx avg `0.2667` n `6`; index avg `-0.0414` n `27`; metal avg `0.2331` n `20`; unknown avg `9.9238` n `1006`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
