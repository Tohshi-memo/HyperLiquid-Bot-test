# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T15:07:27.770856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `13`; crypto_alt avg `-0.0152` n `239`; crypto_major avg `0.0016` n `8`; equity avg `0.7151` n `161`; fx avg `-0.004` n `6`; index avg `0.0515` n `27`; metal avg `-0.0129` n `20`; unknown avg `-0.1411` n `1257`
- 1h: commodity avg `0.1755` n `13`; crypto_alt avg `-0.2627` n `239`; crypto_major avg `-0.3014` n `8`; equity avg `0.354` n `161`; fx avg `-0.0098` n `6`; index avg `0.0101` n `27`; metal avg `-0.1684` n `20`; unknown avg `-0.3794` n `1237`
- 4h: commodity avg `0.235` n `13`; crypto_alt avg `0.2839` n `239`; crypto_major avg `-0.0561` n `8`; equity avg `0.4862` n `161`; fx avg `-0.0371` n `6`; index avg `0.0179` n `27`; metal avg `-0.2873` n `20`; unknown avg `19.3735` n `1231`
- 24h: commodity avg `0.9888` n `13`; crypto_alt avg `-1.5012` n `239`; crypto_major avg `-1.2259` n `8`; equity avg `2.4517` n `161`; fx avg `-0.2317` n `6`; index avg `0.1908` n `27`; metal avg `0.1248` n `20`; unknown avg `1.0334` n `1155`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2992`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
