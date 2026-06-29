# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T07:07:28.509952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0718` n `12`; crypto_alt avg `-0.0889` n `228`; crypto_major avg `-0.1395` n `8`; equity avg `-0.161` n `88`; fx avg `0.0039` n `6`; index avg `-0.0243` n `23`; metal avg `-0.1173` n `20`; unknown avg `-0.0414` n `764`
- 1h: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0353` n `228`; crypto_major avg `-0.225` n `8`; equity avg `0.0544` n `88`; fx avg `0.0582` n `6`; index avg `-0.0073` n `23`; metal avg `-0.0719` n `20`; unknown avg `0.0571` n `764`
- 4h: commodity avg `-0.0735` n `12`; crypto_alt avg `-0.0887` n `228`; crypto_major avg `-0.2986` n `8`; equity avg `0.2989` n `88`; fx avg `0.0181` n `6`; index avg `0.1037` n `23`; metal avg `-0.1086` n `20`; unknown avg `0.0139` n `732`
- 24h: commodity avg `-0.4835` n `12`; crypto_alt avg `0.3527` n `228`; crypto_major avg `0.2245` n `8`; equity avg `0.4069` n `88`; fx avg `0.056` n `6`; index avg `0.0774` n `23`; metal avg `-0.1962` n `20`; unknown avg `-0.6499` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
