# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T00:22:37.201789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0719` n `13`; crypto_alt avg `-0.181` n `239`; crypto_major avg `-0.0975` n `8`; equity avg `-0.2716` n `163`; fx avg `0.0187` n `6`; index avg `-0.0524` n `27`; metal avg `-0.0398` n `20`; unknown avg `0.6714` n `1264`
- 1h: commodity avg `-0.0657` n `13`; crypto_alt avg `-0.1641` n `239`; crypto_major avg `-0.0229` n `8`; equity avg `-0.2794` n `163`; fx avg `-0.0472` n `6`; index avg `-0.0554` n `27`; metal avg `-0.1178` n `20`; unknown avg `2.2003` n `1257`
- 4h: commodity avg `0.0753` n `13`; crypto_alt avg `1.3103` n `239`; crypto_major avg `1.5024` n `8`; equity avg `2.8276` n `163`; fx avg `-0.0527` n `6`; index avg `0.2624` n `27`; metal avg `0.0055` n `20`; unknown avg `2.2646` n `1195`
- 24h: commodity avg `0.2561` n `13`; crypto_alt avg `1.3565` n `239`; crypto_major avg `1.7648` n `8`; equity avg `1.4653` n `163`; fx avg `-0.0287` n `6`; index avg `0.096` n `27`; metal avg `-0.0742` n `20`; unknown avg `7.7006` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1776`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
