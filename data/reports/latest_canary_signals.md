# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T15:37:31.837392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0747` n `12`; crypto_alt avg `-0.0646` n `230`; crypto_major avg `-0.1885` n `8`; equity avg `-0.0609` n `98`; fx avg `-0.0023` n `6`; index avg `0.0071` n `25`; metal avg `0.041` n `20`; unknown avg `-0.0686` n `771`
- 1h: commodity avg `-0.0805` n `12`; crypto_alt avg `0.0222` n `230`; crypto_major avg `-0.2261` n `8`; equity avg `0.2837` n `98`; fx avg `-0.0122` n `6`; index avg `0.099` n `25`; metal avg `0.1383` n `20`; unknown avg `0.0079` n `771`
- 4h: commodity avg `0.1102` n `12`; crypto_alt avg `-0.0559` n `230`; crypto_major avg `-0.2122` n `8`; equity avg `1.2736` n `98`; fx avg `-0.0073` n `6`; index avg `0.2032` n `25`; metal avg `0.1194` n `20`; unknown avg `0.0775` n `771`
- 24h: commodity avg `0.6172` n `12`; crypto_alt avg `1.523` n `230`; crypto_major avg `1.5805` n `8`; equity avg `2.8497` n `98`; fx avg `0.011` n `6`; index avg `0.4121` n `25`; metal avg `0.6979` n `20`; unknown avg `0.2857` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0857`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0571`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0552`, n `666`, weak_sample_signal
