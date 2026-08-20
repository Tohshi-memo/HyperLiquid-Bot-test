# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T01:52:29.884247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5491` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2747` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.1707` n `230`; crypto_major avg `0.2692` n `8`; equity avg `0.158` n `121`; fx avg `0.0036` n `6`; index avg `0.048` n `25`; metal avg `-0.0412` n `20`; unknown avg `0.0225` n `792`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `0.0666` n `230`; crypto_major avg `-0.0897` n `8`; equity avg `0.0599` n `121`; fx avg `0.028` n `6`; index avg `0.0657` n `25`; metal avg `-0.1694` n `20`; unknown avg `0.0398` n `792`
- 4h: commodity avg `0.0445` n `12`; crypto_alt avg `-0.2856` n `230`; crypto_major avg `-1.1212` n `8`; equity avg `0.4279` n `121`; fx avg `0.1108` n `6`; index avg `0.1535` n `25`; metal avg `-0.2604` n `20`; unknown avg `-0.0567` n `792`
- 24h: commodity avg `-0.1212` n `12`; crypto_alt avg `5.5932` n `230`; crypto_major avg `9.9655` n `8`; equity avg `0.7485` n `120`; fx avg `-0.0151` n `6`; index avg `0.2725` n `25`; metal avg `0.9742` n `20`; unknown avg `1.5481` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
