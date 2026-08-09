# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T05:37:35.618098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `-0.1059` n `230`; crypto_major avg `-0.0659` n `8`; equity avg `0.0148` n `112`; fx avg `-0.0009` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.6177` n `784`
- 1h: commodity avg `0.0241` n `12`; crypto_alt avg `-0.4061` n `230`; crypto_major avg `-0.1328` n `8`; equity avg `0.0303` n `112`; fx avg `-0.0022` n `6`; index avg `0.0005` n `25`; metal avg `0.0003` n `20`; unknown avg `0.5332` n `784`
- 4h: commodity avg `0.101` n `12`; crypto_alt avg `0.0802` n `230`; crypto_major avg `-0.1476` n `8`; equity avg `0.0158` n `112`; fx avg `0.0012` n `6`; index avg `0.0084` n `25`; metal avg `0.0016` n `20`; unknown avg `-0.0159` n `784`
- 24h: commodity avg `0.3188` n `12`; crypto_alt avg `1.269` n `230`; crypto_major avg `0.337` n `8`; equity avg `0.5933` n `112`; fx avg `-0.0015` n `6`; index avg `0.0582` n `25`; metal avg `0.0293` n `20`; unknown avg `-0.0145` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
