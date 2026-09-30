# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T21:07:41.421001+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.1742` n `234`; crypto_major avg `-0.0176` n `8`; equity avg `-0.0951` n `142`; fx avg `0.0085` n `6`; index avg `-0.014` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.0178` n `971`
- 1h: commodity avg `-0.0579` n `12`; crypto_alt avg `0.0579` n `234`; crypto_major avg `0.3959` n `8`; equity avg `0.0372` n `142`; fx avg `0.0156` n `6`; index avg `0.0062` n `26`; metal avg `0.0624` n `20`; unknown avg `0.219` n `907`
- 4h: commodity avg `-0.0533` n `12`; crypto_alt avg `-1.4854` n `234`; crypto_major avg `-0.773` n `8`; equity avg `-0.3417` n `142`; fx avg `0.0138` n `6`; index avg `-0.1274` n `26`; metal avg `0.0608` n `20`; unknown avg `1.8726` n `887`
- 24h: commodity avg `0.3218` n `12`; crypto_alt avg `-0.2282` n `234`; crypto_major avg `0.683` n `8`; equity avg `-0.4581` n `142`; fx avg `0.0801` n `6`; index avg `-0.0569` n `26`; metal avg `-0.2104` n `20`; unknown avg `788.2123` n `788`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
