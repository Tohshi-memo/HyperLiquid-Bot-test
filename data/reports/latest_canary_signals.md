# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T03:52:29.008279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0361` n `12`; crypto_alt avg `-0.0073` n `230`; crypto_major avg `0.0971` n `8`; equity avg `-0.0516` n `100`; fx avg `-0.0085` n `6`; index avg `-0.0223` n `25`; metal avg `0.0042` n `20`; unknown avg `0.3487` n `775`
- 1h: commodity avg `-0.0475` n `12`; crypto_alt avg `-0.0231` n `230`; crypto_major avg `0.2171` n `8`; equity avg `0.0645` n `100`; fx avg `-0.0112` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0187` n `20`; unknown avg `0.0094` n `775`
- 4h: commodity avg `0.0591` n `12`; crypto_alt avg `-0.1748` n `230`; crypto_major avg `-0.2914` n `8`; equity avg `-0.3796` n `100`; fx avg `0.1056` n `6`; index avg `-0.2182` n `25`; metal avg `-0.0838` n `20`; unknown avg `-0.0532` n `775`
- 24h: commodity avg `-0.4694` n `12`; crypto_alt avg `1.2275` n `230`; crypto_major avg `1.2665` n `8`; equity avg `0.6823` n `100`; fx avg `0.1289` n `6`; index avg `0.0288` n `25`; metal avg `0.3254` n `20`; unknown avg `-0.0283` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
