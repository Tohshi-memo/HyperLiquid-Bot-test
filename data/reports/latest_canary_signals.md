# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T14:37:29.725647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1078` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `0.3765` n `228`; crypto_major avg `0.3282` n `8`; equity avg `0.64` n `86`; fx avg `-0.0067` n `6`; index avg `0.091` n `23`; metal avg `0.0285` n `20`; unknown avg `0.1168` n `764`
- 1h: commodity avg `0.0755` n `12`; crypto_alt avg `0.0839` n `228`; crypto_major avg `-0.4889` n `8`; equity avg `-0.3192` n `86`; fx avg `-0.0228` n `6`; index avg `0.0001` n `23`; metal avg `0.2384` n `20`; unknown avg `-0.1983` n `764`
- 4h: commodity avg `-0.3679` n `12`; crypto_alt avg `-0.7679` n `228`; crypto_major avg `-1.1182` n `8`; equity avg `-1.2016` n `86`; fx avg `-0.0462` n `6`; index avg `-0.0104` n `23`; metal avg `-0.6917` n `20`; unknown avg `0.2864` n `764`
- 24h: commodity avg `-0.5699` n `12`; crypto_alt avg `-1.8447` n `228`; crypto_major avg `-1.8424` n `8`; equity avg `2.119` n `86`; fx avg `-0.0076` n `6`; index avg `0.0377` n `23`; metal avg `-1.2851` n `20`; unknown avg `-0.4805` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
