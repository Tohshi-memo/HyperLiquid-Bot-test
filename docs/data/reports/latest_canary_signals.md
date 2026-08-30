# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T12:37:24.165770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.042` n `231`; crypto_major avg `0.0092` n `8`; equity avg `-0.0288` n `128`; fx avg `0.0014` n `6`; index avg `0.0262` n `26`; metal avg `0.0071` n `20`; unknown avg `-0.0096` n `793`
- 1h: commodity avg `-0.0218` n `12`; crypto_alt avg `0.4137` n `231`; crypto_major avg `0.3227` n `8`; equity avg `-0.0299` n `128`; fx avg `-0.0004` n `6`; index avg `0.0115` n `26`; metal avg `-0.0139` n `20`; unknown avg `1.1892` n `793`
- 4h: commodity avg `-0.0222` n `12`; crypto_alt avg `0.9108` n `231`; crypto_major avg `0.3458` n `8`; equity avg `-0.0114` n `128`; fx avg `0.0006` n `6`; index avg `0.0297` n `26`; metal avg `-0.0123` n `20`; unknown avg `0.7093` n `789`
- 24h: commodity avg `-0.0491` n `12`; crypto_alt avg `1.8033` n `231`; crypto_major avg `1.2288` n `8`; equity avg `0.2953` n `128`; fx avg `0.0177` n `6`; index avg `0.0825` n `26`; metal avg `0.0838` n `20`; unknown avg `-0.0521` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
