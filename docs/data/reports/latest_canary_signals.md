# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T10:07:30.297105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0548` n `13`; crypto_alt avg `-0.0039` n `238`; crypto_major avg `-0.0223` n `8`; equity avg `-0.0552` n `154`; fx avg `0.0012` n `6`; index avg `-0.0242` n `27`; metal avg `-0.02` n `20`; unknown avg `1.0314` n `1233`
- 1h: commodity avg `0.0513` n `13`; crypto_alt avg `0.2895` n `238`; crypto_major avg `0.2267` n `8`; equity avg `-0.0472` n `154`; fx avg `0.0125` n `6`; index avg `-0.0141` n `27`; metal avg `-0.0544` n `20`; unknown avg `1.7121` n `1200`
- 4h: commodity avg `-0.0026` n `13`; crypto_alt avg `0.5273` n `238`; crypto_major avg `0.7324` n `8`; equity avg `-0.0105` n `154`; fx avg `0.0318` n `6`; index avg `-0.0187` n `27`; metal avg `0.0073` n `20`; unknown avg `56.7945` n `1182`
- 24h: commodity avg `-0.1333` n `13`; crypto_alt avg `3.0185` n `238`; crypto_major avg `3.1491` n `8`; equity avg `3.5037` n `154`; fx avg `0.0846` n `6`; index avg `0.4718` n `27`; metal avg `0.3055` n `20`; unknown avg `8.1997` n `1022`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
