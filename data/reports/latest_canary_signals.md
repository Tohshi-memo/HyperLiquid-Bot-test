# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T08:37:25.119559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.64` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.1384` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9323` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.9285` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0696` n `12`; crypto_alt avg `0.0588` n `228`; crypto_major avg `0.1181` n `8`; equity avg `-0.0309` n `69`; fx avg `0.0048` n `6`; index avg `0.0535` n `23`; metal avg `-0.1177` n `18`; unknown avg `0.8353` n `422`
- 1h: commodity avg `-0.2354` n `12`; crypto_alt avg `-0.0882` n `228`; crypto_major avg `-0.2435` n `8`; equity avg `0.2244` n `69`; fx avg `-0.011` n `6`; index avg `0.1765` n `23`; metal avg `-0.0232` n `18`; unknown avg `-0.0195` n `422`
- 4h: commodity avg `-0.1711` n `12`; crypto_alt avg `-1.14` n `228`; crypto_major avg `-1.3221` n `8`; equity avg `0.6102` n `69`; fx avg `0.033` n `6`; index avg `0.6064` n `23`; metal avg `0.8163` n `18`; unknown avg `0.1241` n `412`
- 24h: commodity avg `-1.3226` n `12`; crypto_alt avg `0.2111` n `228`; crypto_major avg `-1.1577` n `8`; equity avg `0.8278` n `69`; fx avg `0.144` n `6`; index avg `0.1485` n `23`; metal avg `1.317` n `18`; unknown avg `1.9679` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
