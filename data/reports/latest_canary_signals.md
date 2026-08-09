# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T06:04:08.498567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `0.0864` n `230`; crypto_major avg `0.0668` n `8`; equity avg `0.0704` n `112`; fx avg `0.0` n `6`; index avg `-0.0015` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0199` n `752`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.1556` n `230`; crypto_major avg `-0.0259` n `8`; equity avg `0.0776` n `112`; fx avg `-0.0087` n `6`; index avg `-0.0114` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0241` n `752`
- 4h: commodity avg `0.0806` n `12`; crypto_alt avg `0.1666` n `230`; crypto_major avg `-0.0451` n `8`; equity avg `0.0531` n `112`; fx avg `-0.0038` n `6`; index avg `0.003` n `25`; metal avg `0.0159` n `20`; unknown avg `-0.018` n `752`
- 24h: commodity avg `0.283` n `12`; crypto_alt avg `1.4956` n `230`; crypto_major avg `0.4507` n `8`; equity avg `0.6884` n `112`; fx avg `-0.0145` n `6`; index avg `0.0752` n `25`; metal avg `0.0318` n `20`; unknown avg `-0.0216` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
