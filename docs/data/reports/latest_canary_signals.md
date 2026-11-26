# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T08:07:39.056665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `13`; crypto_alt avg `0.0578` n `239`; crypto_major avg `0.0703` n `8`; equity avg `-0.0052` n `168`; fx avg `0.0261` n `6`; index avg `-0.0035` n `27`; metal avg `0.0697` n `20`; unknown avg `0.1414` n `1241`
- 1h: commodity avg `0.0369` n `13`; crypto_alt avg `0.0871` n `239`; crypto_major avg `0.135` n `8`; equity avg `0.0948` n `168`; fx avg `0.037` n `6`; index avg `0.0156` n `27`; metal avg `0.0189` n `20`; unknown avg `203.5884` n `1247`
- 4h: commodity avg `-0.2587` n `13`; crypto_alt avg `-0.3588` n `239`; crypto_major avg `-0.5869` n `8`; equity avg `-0.7141` n `168`; fx avg `0.0525` n `6`; index avg `-0.0643` n `27`; metal avg `-0.1363` n `20`; unknown avg `0.1054` n `1209`
- 24h: commodity avg `0.7881` n `13`; crypto_alt avg `3.0065` n `239`; crypto_major avg `3.3454` n `8`; equity avg `3.0852` n `168`; fx avg `0.1062` n `6`; index avg `0.2328` n `27`; metal avg `0.7141` n `20`; unknown avg `760.7537` n `1033`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
