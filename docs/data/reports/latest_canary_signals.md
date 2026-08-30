# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T08:37:25.606861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `-0.0898` n `231`; crypto_major avg `-0.0426` n `8`; equity avg `0.0082` n `128`; fx avg `0.0` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.0887` n `793`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `-0.0753` n `231`; crypto_major avg `-0.0415` n `8`; equity avg `0.0076` n `128`; fx avg `-0.0` n `6`; index avg `-0.0137` n `26`; metal avg `0.0017` n `20`; unknown avg `0.0361` n `793`
- 4h: commodity avg `0.0037` n `12`; crypto_alt avg `0.2096` n `231`; crypto_major avg `0.045` n `8`; equity avg `0.0189` n `128`; fx avg `0.005` n `6`; index avg `0.0072` n `26`; metal avg `0.011` n `20`; unknown avg `0.0729` n `759`
- 24h: commodity avg `0.0026` n `12`; crypto_alt avg `0.9709` n `231`; crypto_major avg `1.0099` n `8`; equity avg `0.2823` n `128`; fx avg `-0.0171` n `6`; index avg `0.0492` n `26`; metal avg `0.0893` n `20`; unknown avg `0.3139` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
