# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T01:37:26.443141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `-0.0142` n `239`; crypto_major avg `0.0169` n `8`; equity avg `-0.0303` n `168`; fx avg `-0.0026` n `6`; index avg `-0.004` n `27`; metal avg `-0.0039` n `20`; unknown avg `1.7318` n `1265`
- 1h: commodity avg `0.1072` n `13`; crypto_alt avg `0.1581` n `239`; crypto_major avg `0.3822` n `8`; equity avg `0.0687` n `168`; fx avg `0.0058` n `6`; index avg `0.0053` n `27`; metal avg `-0.0069` n `20`; unknown avg `34.2361` n `1259`
- 4h: commodity avg `-0.0823` n `13`; crypto_alt avg `0.2053` n `239`; crypto_major avg `0.3364` n `8`; equity avg `0.0696` n `168`; fx avg `-0.0076` n `6`; index avg `-0.0023` n `27`; metal avg `0.0147` n `20`; unknown avg `0.5393` n `1227`
- 24h: commodity avg `-0.6933` n `13`; crypto_alt avg `0.2407` n `239`; crypto_major avg `0.4657` n `8`; equity avg `2.3572` n `168`; fx avg `-0.1447` n `6`; index avg `0.2231` n `27`; metal avg `0.8478` n `20`; unknown avg `291.5282` n `989`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
