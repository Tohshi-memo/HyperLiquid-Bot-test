# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T16:37:26.307991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6825` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0653` n `12`; crypto_alt avg `0.0908` n `230`; crypto_major avg `0.0598` n `8`; equity avg `0.1272` n `94`; fx avg `-0.0108` n `6`; index avg `0.0136` n `25`; metal avg `0.0409` n `20`; unknown avg `0.0119` n `768`
- 1h: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.2026` n `230`; crypto_major avg `-0.521` n `8`; equity avg `-0.5891` n `94`; fx avg `-0.0351` n `6`; index avg `-0.1246` n `25`; metal avg `-0.1736` n `20`; unknown avg `-0.2403` n `768`
- 4h: commodity avg `-0.4865` n `12`; crypto_alt avg `0.6031` n `230`; crypto_major avg `0.2888` n `8`; equity avg `-1.3937` n `94`; fx avg `-0.0393` n `6`; index avg `-0.0075` n `25`; metal avg `-0.1045` n `20`; unknown avg `-0.0819` n `768`
- 24h: commodity avg `-0.1725` n `12`; crypto_alt avg `0.1085` n `230`; crypto_major avg `-0.7996` n `8`; equity avg `-1.9367` n `94`; fx avg `-0.1097` n `6`; index avg `-0.1459` n `25`; metal avg `-0.1153` n `20`; unknown avg `-0.1765` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
