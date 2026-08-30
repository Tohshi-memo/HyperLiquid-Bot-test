# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T12:22:24.662790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0347` n `12`; crypto_alt avg `-0.0706` n `231`; crypto_major avg `-0.0037` n `8`; equity avg `-0.013` n `128`; fx avg `-0.0031` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.0137` n `793`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `0.2804` n `231`; crypto_major avg `0.2255` n `8`; equity avg `-0.0049` n `128`; fx avg `-0.0016` n `6`; index avg `-0.0214` n `26`; metal avg `-0.0163` n `20`; unknown avg `1.2775` n `793`
- 4h: commodity avg `-0.0164` n `12`; crypto_alt avg `0.7708` n `231`; crypto_major avg `0.2937` n `8`; equity avg `0.0255` n `128`; fx avg `-0.0009` n `6`; index avg `0.003` n `26`; metal avg `-0.0256` n `20`; unknown avg `0.8448` n `789`
- 24h: commodity avg `-0.0499` n `12`; crypto_alt avg `1.6505` n `231`; crypto_major avg `1.0896` n `8`; equity avg `0.3016` n `128`; fx avg `0.0117` n `6`; index avg `0.049` n `26`; metal avg `0.0711` n `20`; unknown avg `-0.0572` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
