# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T11:22:36.405243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0607` n `12`; crypto_alt avg `-0.2036` n `228`; crypto_major avg `-0.2512` n `8`; equity avg `-0.0989` n `88`; fx avg `-0.0018` n `6`; index avg `-0.0231` n `23`; metal avg `-0.0341` n `20`; unknown avg `0.1833` n `764`
- 1h: commodity avg `0.0959` n `12`; crypto_alt avg `-0.4497` n `228`; crypto_major avg `-0.5922` n `8`; equity avg `-0.067` n `88`; fx avg `0.0056` n `6`; index avg `0.0022` n `23`; metal avg `-0.0349` n `20`; unknown avg `0.1173` n `764`
- 4h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.2732` n `228`; crypto_major avg `-0.1229` n `8`; equity avg `0.1427` n `88`; fx avg `0.0292` n `6`; index avg `0.026` n `23`; metal avg `-0.3473` n `20`; unknown avg `0.1456` n `764`
- 24h: commodity avg `-0.3831` n `12`; crypto_alt avg `-0.1777` n `228`; crypto_major avg `-0.4427` n `8`; equity avg `0.3754` n `88`; fx avg `0.0708` n `6`; index avg `0.0686` n `23`; metal avg `-0.5424` n `20`; unknown avg `0.9907` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
