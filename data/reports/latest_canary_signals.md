# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T18:07:32.272861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `-0.3965` n `234`; crypto_major avg `-0.2619` n `8`; equity avg `-0.0204` n `142`; fx avg `-0.0048` n `6`; index avg `-0.0216` n `26`; metal avg `-0.0151` n `20`; unknown avg `-0.241` n `967`
- 1h: commodity avg `0.0516` n `12`; crypto_alt avg `-0.9773` n `234`; crypto_major avg `-0.8706` n `8`; equity avg `-0.1755` n `142`; fx avg `-0.0035` n `6`; index avg `-0.0489` n `26`; metal avg `-0.0532` n `20`; unknown avg `0.5941` n `967`
- 4h: commodity avg `0.1225` n `12`; crypto_alt avg `-1.1192` n `234`; crypto_major avg `-0.4384` n `8`; equity avg `-0.4031` n `142`; fx avg `0.012` n `6`; index avg `-0.1208` n `26`; metal avg `-0.2359` n `20`; unknown avg `3.5555` n `903`
- 24h: commodity avg `0.2838` n `12`; crypto_alt avg `1.0822` n `234`; crypto_major avg `1.0175` n `8`; equity avg `-0.1693` n `142`; fx avg `0.0688` n `6`; index avg `0.0847` n `26`; metal avg `-0.1436` n `20`; unknown avg `4.2033` n `820`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
