# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T14:37:30.470472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0766` n `13`; crypto_alt avg `-0.0866` n `239`; crypto_major avg `-0.0027` n `8`; equity avg `0.0658` n `168`; fx avg `-0.0102` n `6`; index avg `0.0154` n `27`; metal avg `0.074` n `20`; unknown avg `-0.0964` n `1267`
- 1h: commodity avg `-0.0141` n `13`; crypto_alt avg `0.0195` n `239`; crypto_major avg `0.0575` n `8`; equity avg `-0.1491` n `168`; fx avg `0.0036` n `6`; index avg `-0.028` n `27`; metal avg `0.0709` n `20`; unknown avg `271.6231` n `1265`
- 4h: commodity avg `0.1833` n `13`; crypto_alt avg `0.1195` n `239`; crypto_major avg `0.2122` n `8`; equity avg `0.2607` n `168`; fx avg `-0.0089` n `6`; index avg `0.0212` n `27`; metal avg `0.0987` n `20`; unknown avg `1.0872` n `1253`
- 24h: commodity avg `0.2937` n `13`; crypto_alt avg `5.9417` n `239`; crypto_major avg `5.4603` n `8`; equity avg `6.3732` n `168`; fx avg `0.0777` n `6`; index avg `0.5801` n `27`; metal avg `1.2623` n `20`; unknown avg `74.0645` n `1061`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
