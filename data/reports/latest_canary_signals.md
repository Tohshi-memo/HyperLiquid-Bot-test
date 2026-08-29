# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T13:22:25.477694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `0.1687` n `231`; crypto_major avg `0.1142` n `8`; equity avg `0.0362` n `127`; fx avg `-0.0031` n `6`; index avg `0.0128` n `26`; metal avg `0.0121` n `20`; unknown avg `0.0098` n `793`
- 1h: commodity avg `0.0109` n `12`; crypto_alt avg `0.0765` n `231`; crypto_major avg `0.0268` n `8`; equity avg `-0.0113` n `127`; fx avg `-0.0037` n `6`; index avg `-0.0025` n `26`; metal avg `0.0156` n `20`; unknown avg `0.122` n `791`
- 4h: commodity avg `0.0305` n `12`; crypto_alt avg `0.3238` n `231`; crypto_major avg `0.2274` n `8`; equity avg `-0.0178` n `127`; fx avg `-0.0231` n `6`; index avg `0.0059` n `26`; metal avg `0.005` n `20`; unknown avg `0.083` n `759`
- 24h: commodity avg `0.1165` n `12`; crypto_alt avg `-1.6651` n `231`; crypto_major avg `-1.8858` n `8`; equity avg `-1.3403` n `127`; fx avg `-0.0649` n `6`; index avg `-0.1544` n `26`; metal avg `-0.7855` n `20`; unknown avg `-0.5089` n `743`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
