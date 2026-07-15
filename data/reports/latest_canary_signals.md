# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T14:22:26.786463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.067` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `-0.2614` n `230`; crypto_major avg `-0.2057` n `8`; equity avg `-0.8873` n `93`; fx avg `-0.0024` n `6`; index avg `-0.1208` n `25`; metal avg `-0.0438` n `20`; unknown avg `-0.0117` n `768`
- 1h: commodity avg `-0.0829` n `12`; crypto_alt avg `-0.6596` n `230`; crypto_major avg `-0.5583` n `8`; equity avg `-1.1964` n `93`; fx avg `0.0259` n `6`; index avg `-0.2189` n `25`; metal avg `-0.0187` n `20`; unknown avg `0.0729` n `768`
- 4h: commodity avg `-0.187` n `12`; crypto_alt avg `0.6032` n `230`; crypto_major avg `0.9233` n `8`; equity avg `-1.1437` n `93`; fx avg `0.0542` n `6`; index avg `-0.2201` n `25`; metal avg `0.2268` n `20`; unknown avg `0.0973` n `767`
- 24h: commodity avg `0.0246` n `12`; crypto_alt avg `0.835` n `230`; crypto_major avg `1.9921` n `8`; equity avg `0.0482` n `92`; fx avg `0.0753` n `6`; index avg `-0.0114` n `25`; metal avg `-0.1137` n `20`; unknown avg `0.1929` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
