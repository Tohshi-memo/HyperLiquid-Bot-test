# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T20:07:31.614648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0634` n `13`; crypto_alt avg `0.4206` n `239`; crypto_major avg `0.2832` n `8`; equity avg `0.3819` n `157`; fx avg `0.0045` n `6`; index avg `0.0483` n `27`; metal avg `0.047` n `20`; unknown avg `2.3701` n `1236`
- 1h: commodity avg `-0.0284` n `13`; crypto_alt avg `0.0417` n `239`; crypto_major avg `0.2147` n `8`; equity avg `-0.1476` n `157`; fx avg `0.0072` n `6`; index avg `-0.0383` n `27`; metal avg `-0.032` n `20`; unknown avg `21.4375` n `1236`
- 4h: commodity avg `-0.4412` n `13`; crypto_alt avg `-1.5151` n `239`; crypto_major avg `-1.048` n `8`; equity avg `-2.2561` n `157`; fx avg `0.0083` n `6`; index avg `-0.2166` n `27`; metal avg `-0.1555` n `20`; unknown avg `0.0413` n `1170`
- 24h: commodity avg `-1.3793` n `13`; crypto_alt avg `-2.6802` n `238`; crypto_major avg `-1.3055` n `8`; equity avg `-2.3898` n `157`; fx avg `0.2645` n `6`; index avg `0.0785` n `27`; metal avg `0.2481` n `20`; unknown avg `3.9274` n `1016`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
