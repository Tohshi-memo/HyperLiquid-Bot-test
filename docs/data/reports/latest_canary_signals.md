# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T23:22:38.003636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.021` n `12`; crypto_alt avg `-0.3282` n `234`; crypto_major avg `-0.1574` n `8`; equity avg `0.0125` n `142`; fx avg `0.0014` n `6`; index avg `0.0025` n `26`; metal avg `0.0025` n `20`; unknown avg `0.5033` n `963`
- 1h: commodity avg `0.1191` n `12`; crypto_alt avg `0.0596` n `234`; crypto_major avg `0.0519` n `8`; equity avg `-0.0313` n `142`; fx avg `0.0011` n `6`; index avg `-0.029` n `26`; metal avg `-0.0092` n `20`; unknown avg `0.8923` n `960`
- 4h: commodity avg `0.0096` n `12`; crypto_alt avg `-0.1934` n `234`; crypto_major avg `-0.0107` n `8`; equity avg `0.1313` n `142`; fx avg `0.0008` n `6`; index avg `0.0298` n `26`; metal avg `0.0862` n `20`; unknown avg `-0.3195` n `872`
- 24h: commodity avg `-0.8711` n `12`; crypto_alt avg `0.4566` n `234`; crypto_major avg `-0.0393` n `8`; equity avg `0.7367` n `142`; fx avg `-0.145` n `6`; index avg `0.0816` n `26`; metal avg `0.257` n `20`; unknown avg `3099.1928` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
