# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T17:07:31.240439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0883` n `13`; crypto_alt avg `0.2376` n `234`; crypto_major avg `0.2808` n `8`; equity avg `0.0464` n `142`; fx avg `-0.0165` n `6`; index avg `0.017` n `26`; metal avg `0.0573` n `20`; unknown avg `0.3013` n `973`
- 1h: commodity avg `0.0111` n `13`; crypto_alt avg `-0.2591` n `234`; crypto_major avg `0.0361` n `8`; equity avg `0.1881` n `142`; fx avg `-0.0435` n `6`; index avg `0.0462` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.1301` n `973`
- 4h: commodity avg `0.1207` n `13`; crypto_alt avg `0.004` n `234`; crypto_major avg `0.0649` n `8`; equity avg `-0.0305` n `142`; fx avg `-0.165` n `6`; index avg `-0.1163` n `26`; metal avg `-0.1363` n `20`; unknown avg `1.1885` n `909`
- 24h: commodity avg `-0.1376` n `13`; crypto_alt avg `-1.9315` n `234`; crypto_major avg `-1.118` n `8`; equity avg `0.1257` n `142`; fx avg `-0.1329` n `6`; index avg `-0.0499` n `26`; metal avg `-0.0864` n `20`; unknown avg `0.1073` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
