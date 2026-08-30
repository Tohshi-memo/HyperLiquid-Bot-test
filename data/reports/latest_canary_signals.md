# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T22:07:23.282814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0303` n `12`; crypto_alt avg `0.2857` n `231`; crypto_major avg `0.1641` n `8`; equity avg `-0.0996` n `128`; fx avg `-0.0186` n `6`; index avg `-0.0689` n `26`; metal avg `-0.1603` n `20`; unknown avg `-0.0522` n `791`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `0.5822` n `231`; crypto_major avg `0.2716` n `8`; equity avg `-0.0743` n `128`; fx avg `-0.0156` n `6`; index avg `-0.0641` n `26`; metal avg `-0.2042` n `20`; unknown avg `0.7545` n `791`
- 4h: commodity avg `0.4261` n `12`; crypto_alt avg `-0.3989` n `231`; crypto_major avg `-0.9296` n `8`; equity avg `-0.282` n `128`; fx avg `-0.0154` n `6`; index avg `-0.1179` n `26`; metal avg `-0.275` n `20`; unknown avg `0.2712` n `791`
- 24h: commodity avg `0.4782` n `12`; crypto_alt avg `1.2182` n `231`; crypto_major avg `0.048` n `8`; equity avg `-0.0981` n `128`; fx avg `0.0181` n `6`; index avg `-0.056` n `26`; metal avg `-0.1799` n `20`; unknown avg `0.0574` n `745`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
