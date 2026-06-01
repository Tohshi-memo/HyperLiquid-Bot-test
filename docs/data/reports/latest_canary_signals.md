# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T14:22:28.183038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1223` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0458` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.069` n `12`; crypto_alt avg `0.0426` n `228`; crypto_major avg `-0.1896` n `8`; equity avg `-0.0482` n `69`; fx avg `0.0067` n `6`; index avg `-0.019` n `23`; metal avg `0.1025` n `18`; unknown avg `-0.0718` n `422`
- 1h: commodity avg `0.5648` n `12`; crypto_alt avg `-0.3998` n `228`; crypto_major avg `-1.0455` n `8`; equity avg `0.0754` n `69`; fx avg `-0.0591` n `6`; index avg `0.0003` n `23`; metal avg `-0.1667` n `18`; unknown avg `-0.3811` n `422`
- 4h: commodity avg `0.2501` n `12`; crypto_alt avg `-0.7657` n `228`; crypto_major avg `-1.4424` n `8`; equity avg `-0.6708` n `69`; fx avg `-0.0873` n `6`; index avg `-0.3201` n `23`; metal avg `-0.9114` n `18`; unknown avg `2.4546` n `416`
- 24h: commodity avg `1.2481` n `12`; crypto_alt avg `-0.2817` n `228`; crypto_major avg `-1.749` n `8`; equity avg `-0.7779` n `69`; fx avg `-0.0716` n `6`; index avg `0.2377` n `23`; metal avg `-0.6708` n `18`; unknown avg `4.2722` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2826`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
