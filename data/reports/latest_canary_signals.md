# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T13:37:32.060943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0405` n `13`; crypto_alt avg `-0.0623` n `238`; crypto_major avg `-0.1898` n `8`; equity avg `0.1638` n `156`; fx avg `-0.0083` n `6`; index avg `0.0146` n `27`; metal avg `-0.0298` n `20`; unknown avg `1.0602` n `1261`
- 1h: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.3722` n `238`; crypto_major avg `-0.4504` n `8`; equity avg `0.1313` n `156`; fx avg `-0.0419` n `6`; index avg `0.0296` n `27`; metal avg `-0.0918` n `20`; unknown avg `91.1654` n `1251`
- 4h: commodity avg `-0.0436` n `13`; crypto_alt avg `0.2996` n `238`; crypto_major avg `-0.3642` n `8`; equity avg `-0.8618` n `156`; fx avg `-0.0913` n `6`; index avg `-0.0549` n `27`; metal avg `-0.3526` n `20`; unknown avg `1.8379` n `1247`
- 24h: commodity avg `0.589` n `13`; crypto_alt avg `-4.3312` n `238`; crypto_major avg `-3.2242` n `8`; equity avg `-3.991` n `156`; fx avg `0.0531` n `6`; index avg `-0.3131` n `27`; metal avg `-0.7792` n `20`; unknown avg `3442.5469` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
