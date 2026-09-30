# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T22:37:26.776842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0261` n `12`; crypto_alt avg `0.4457` n `234`; crypto_major avg `0.1639` n `8`; equity avg `0.0748` n `142`; fx avg `0.0072` n `6`; index avg `0.0153` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.0185` n `975`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `0.4873` n `234`; crypto_major avg `0.16` n `8`; equity avg `0.2533` n `142`; fx avg `-0.0074` n `6`; index avg `0.0661` n `26`; metal avg `-0.0081` n `20`; unknown avg `-0.158` n `973`
- 4h: commodity avg `-0.1916` n `12`; crypto_alt avg `0.5393` n `234`; crypto_major avg `0.5834` n `8`; equity avg `0.124` n `142`; fx avg `0.0318` n `6`; index avg `-0.0054` n `26`; metal avg `0.0449` n `20`; unknown avg `1.7051` n `887`
- 24h: commodity avg `0.1272` n `12`; crypto_alt avg `0.7738` n `234`; crypto_major avg `0.9926` n `8`; equity avg `-0.3462` n `142`; fx avg `0.0727` n `6`; index avg `-0.0419` n `26`; metal avg `-0.2279` n `20`; unknown avg `764.1353` n `812`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
