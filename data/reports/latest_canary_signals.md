# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T03:52:26.410943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `-0.0249` n `239`; crypto_major avg `0.0499` n `8`; equity avg `-0.0353` n `161`; fx avg `-0.0116` n `6`; index avg `0.007` n `27`; metal avg `0.0082` n `20`; unknown avg `0.1129` n `1260`
- 1h: commodity avg `-0.0706` n `13`; crypto_alt avg `-0.2168` n `239`; crypto_major avg `-0.2527` n `8`; equity avg `-0.5325` n `161`; fx avg `-0.0265` n `6`; index avg `-0.0558` n `27`; metal avg `0.018` n `20`; unknown avg `18.8756` n `1252`
- 4h: commodity avg `-0.0584` n `13`; crypto_alt avg `-0.1731` n `239`; crypto_major avg `-0.1803` n `8`; equity avg `-0.1302` n `161`; fx avg `-0.1127` n `6`; index avg `0.0036` n `27`; metal avg `0.0842` n `20`; unknown avg `19.5306` n `1246`
- 24h: commodity avg `0.079` n `13`; crypto_alt avg `-1.9192` n `239`; crypto_major avg `-0.5635` n `8`; equity avg `0.5203` n `161`; fx avg `-0.2096` n `6`; index avg `0.0244` n `27`; metal avg `-0.4004` n `20`; unknown avg `0.4518` n `1137`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
