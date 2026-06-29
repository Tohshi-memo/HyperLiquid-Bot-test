# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T05:37:30.639321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.069` n `12`; crypto_alt avg `0.0486` n `228`; crypto_major avg `0.1006` n `8`; equity avg `0.1207` n `88`; fx avg `0.0048` n `6`; index avg `0.0379` n `23`; metal avg `-0.1716` n `20`; unknown avg `-0.0045` n `764`
- 1h: commodity avg `-0.1569` n `12`; crypto_alt avg `-0.3959` n `228`; crypto_major avg `-0.3446` n `8`; equity avg `0.0925` n `88`; fx avg `0.0099` n `6`; index avg `0.1004` n `23`; metal avg `-0.208` n `20`; unknown avg `4.3773` n `764`
- 4h: commodity avg `-0.204` n `12`; crypto_alt avg `0.2919` n `228`; crypto_major avg `0.1538` n `8`; equity avg `0.1392` n `88`; fx avg `0.0579` n `6`; index avg `0.049` n `23`; metal avg `-0.2327` n `20`; unknown avg `-0.6982` n `764`
- 24h: commodity avg `-0.4442` n `12`; crypto_alt avg `-0.1257` n `228`; crypto_major avg `-0.1441` n `8`; equity avg `0.0831` n `88`; fx avg `0.0739` n `6`; index avg `0.0041` n `23`; metal avg `-0.4584` n `20`; unknown avg `-0.9789` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
