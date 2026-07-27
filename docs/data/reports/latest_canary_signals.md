# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T08:07:27.279990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0544` n `230`; crypto_major avg `-0.0738` n `8`; equity avg `-0.0079` n `100`; fx avg `0.003` n `6`; index avg `-0.005` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.0211` n `775`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `-0.1448` n `230`; crypto_major avg `-0.2033` n `8`; equity avg `-0.0518` n `100`; fx avg `-0.023` n `6`; index avg `-0.0171` n `25`; metal avg `-0.0383` n `20`; unknown avg `-0.0005` n `775`
- 4h: commodity avg `-0.2833` n `12`; crypto_alt avg `-0.2505` n `230`; crypto_major avg `-0.0123` n `8`; equity avg `0.6406` n `100`; fx avg `0.0043` n `6`; index avg `0.1184` n `25`; metal avg `0.1296` n `20`; unknown avg `-0.0165` n `759`
- 24h: commodity avg `-0.7583` n `12`; crypto_alt avg `0.6548` n `230`; crypto_major avg `1.3884` n `8`; equity avg `1.3634` n `100`; fx avg `0.1142` n `6`; index avg `0.1685` n `25`; metal avg `0.4273` n `20`; unknown avg `-0.0873` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
