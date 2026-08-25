# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T19:52:39.277033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0913` n `12`; crypto_alt avg `0.2183` n `231`; crypto_major avg `0.2249` n `8`; equity avg `0.15` n `122`; fx avg `-0.0052` n `6`; index avg `0.016` n `25`; metal avg `0.0325` n `20`; unknown avg `0.1822` n `795`
- 1h: commodity avg `-0.1152` n `12`; crypto_alt avg `-0.5059` n `231`; crypto_major avg `-0.3569` n `8`; equity avg `-0.0054` n `122`; fx avg `-0.0186` n `6`; index avg `-0.0044` n `25`; metal avg `0.1115` n `20`; unknown avg `0.0026` n `795`
- 4h: commodity avg `0.0451` n `12`; crypto_alt avg `-0.465` n `231`; crypto_major avg `-0.3031` n `8`; equity avg `0.0983` n `122`; fx avg `-0.0113` n `6`; index avg `0.0203` n `25`; metal avg `0.1281` n `20`; unknown avg `-0.1815` n `795`
- 24h: commodity avg `-0.6414` n `12`; crypto_alt avg `-0.6967` n `231`; crypto_major avg `0.7047` n `8`; equity avg `2.081` n `122`; fx avg `0.037` n `6`; index avg `0.2321` n `25`; metal avg `0.0326` n `20`; unknown avg `-0.4808` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
