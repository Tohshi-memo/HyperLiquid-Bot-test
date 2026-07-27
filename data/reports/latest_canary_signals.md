# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T11:07:24.340062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0708` n `12`; crypto_alt avg `-0.0787` n `230`; crypto_major avg `-0.0661` n `8`; equity avg `-0.1399` n `100`; fx avg `-0.0065` n `6`; index avg `-0.019` n `25`; metal avg `-0.0401` n `20`; unknown avg `-0.0645` n `776`
- 1h: commodity avg `0.1663` n `12`; crypto_alt avg `0.0206` n `230`; crypto_major avg `0.1128` n `8`; equity avg `-0.2254` n `100`; fx avg `-0.0125` n `6`; index avg `-0.0196` n `25`; metal avg `-0.0069` n `20`; unknown avg `-0.0461` n `775`
- 4h: commodity avg `-0.0988` n `12`; crypto_alt avg `-0.2965` n `230`; crypto_major avg `-0.1269` n `8`; equity avg `-0.044` n `100`; fx avg `-0.0504` n `6`; index avg `0.011` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.1454` n `775`
- 24h: commodity avg `-0.5857` n `12`; crypto_alt avg `0.5964` n `230`; crypto_major avg `1.2977` n `8`; equity avg `1.1513` n `100`; fx avg `0.0847` n `6`; index avg `0.1375` n `25`; metal avg `0.3458` n `20`; unknown avg `-0.1965` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
