# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T06:37:26.207565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0848` n `12`; crypto_alt avg `-0.171` n `228`; crypto_major avg `-0.3444` n `8`; equity avg `0.107` n `88`; fx avg `0.0227` n `6`; index avg `0.0071` n `23`; metal avg `-0.011` n `20`; unknown avg `0.1403` n `764`
- 1h: commodity avg `0.2183` n `12`; crypto_alt avg `0.7229` n `228`; crypto_major avg `0.7209` n `8`; equity avg `0.5102` n `88`; fx avg `0.0191` n `6`; index avg `0.0977` n `23`; metal avg `0.3698` n `20`; unknown avg `0.4616` n `732`
- 4h: commodity avg `0.0962` n `12`; crypto_alt avg `0.7245` n `228`; crypto_major avg `0.5341` n `8`; equity avg `0.7616` n `88`; fx avg `0.037` n `6`; index avg `0.1832` n `23`; metal avg `0.0937` n `20`; unknown avg `0.1109` n `732`
- 24h: commodity avg `-0.2674` n `12`; crypto_alt avg `0.7758` n `228`; crypto_major avg `0.6241` n `8`; equity avg `0.572` n `88`; fx avg `0.0799` n `6`; index avg `0.1177` n `23`; metal avg `-0.1312` n `20`; unknown avg `-0.5619` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
