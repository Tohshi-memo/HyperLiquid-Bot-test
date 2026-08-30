# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T11:22:28.216692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `0.0345` n `231`; crypto_major avg `-0.0622` n `8`; equity avg `0.0159` n `128`; fx avg `0.0034` n `6`; index avg `0.0203` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.0731` n `791`
- 1h: commodity avg `-0.0107` n `12`; crypto_alt avg `0.2229` n `231`; crypto_major avg `0.167` n `8`; equity avg `0.0301` n `128`; fx avg `0.0002` n `6`; index avg `0.0135` n `26`; metal avg `0.0018` n `20`; unknown avg `-0.0373` n `789`
- 4h: commodity avg `-0.0146` n `12`; crypto_alt avg `0.4352` n `231`; crypto_major avg `-0.0269` n `8`; equity avg `0.0143` n `128`; fx avg `-0.0009` n `6`; index avg `0.0087` n `26`; metal avg `-0.0042` n `20`; unknown avg `-0.3512` n `789`
- 24h: commodity avg `-0.0359` n `12`; crypto_alt avg `1.52` n `231`; crypto_major avg `0.9446` n `8`; equity avg `0.2762` n `128`; fx avg `0.0115` n `6`; index avg `0.0813` n `26`; metal avg `0.0967` n `20`; unknown avg `0.8217` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
