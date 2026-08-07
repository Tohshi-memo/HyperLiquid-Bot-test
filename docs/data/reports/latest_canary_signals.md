# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T13:07:32.947617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.055` n `12`; crypto_alt avg `0.0256` n `230`; crypto_major avg `0.0261` n `8`; equity avg `-0.2278` n `112`; fx avg `0.0147` n `6`; index avg `-0.0472` n `25`; metal avg `-0.1584` n `20`; unknown avg `-0.0227` n `782`
- 1h: commodity avg `0.0663` n `12`; crypto_alt avg `-0.0651` n `230`; crypto_major avg `0.2209` n `8`; equity avg `0.9124` n `112`; fx avg `-0.0621` n `6`; index avg `0.1187` n `25`; metal avg `0.0861` n `20`; unknown avg `-0.053` n `782`
- 4h: commodity avg `-0.1672` n `12`; crypto_alt avg `0.0841` n `230`; crypto_major avg `0.7022` n `8`; equity avg `0.9964` n `112`; fx avg `-0.0584` n `6`; index avg `0.1435` n `25`; metal avg `-0.0694` n `20`; unknown avg `0.0294` n `782`
- 24h: commodity avg `0.0402` n `12`; crypto_alt avg `0.8343` n `230`; crypto_major avg `1.2649` n `8`; equity avg `3.6534` n `109`; fx avg `-0.1381` n `6`; index avg `0.3071` n `25`; metal avg `0.5072` n `20`; unknown avg `0.3625` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
