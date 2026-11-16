# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T08:52:33.286588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0838` n `13`; crypto_alt avg `0.0783` n `239`; crypto_major avg `0.0288` n `8`; equity avg `0.0746` n `162`; fx avg `0.0315` n `6`; index avg `0.0169` n `27`; metal avg `0.0567` n `20`; unknown avg `1.1782` n `1265`
- 1h: commodity avg `-0.0845` n `13`; crypto_alt avg `-0.2749` n `239`; crypto_major avg `-0.4216` n `8`; equity avg `0.0732` n `162`; fx avg `0.0119` n `6`; index avg `0.0427` n `27`; metal avg `0.0533` n `20`; unknown avg `2.8239` n `1219`
- 4h: commodity avg `-0.0599` n `13`; crypto_alt avg `-0.5109` n `239`; crypto_major avg `-0.2392` n `8`; equity avg `-0.1645` n `162`; fx avg `-0.0124` n `6`; index avg `0.0388` n `27`; metal avg `-0.0075` n `20`; unknown avg `2.0707` n `1077`
- 24h: commodity avg `-0.4003` n `13`; crypto_alt avg `0.1804` n `239`; crypto_major avg `0.4096` n `8`; equity avg `-0.1157` n `162`; fx avg `-0.0399` n `6`; index avg `0.0424` n `27`; metal avg `0.0624` n `20`; unknown avg `2.6814` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
