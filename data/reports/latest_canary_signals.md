# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T16:37:33.759201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0218` n `12`; crypto_alt avg `-0.169` n `234`; crypto_major avg `-0.0441` n `8`; equity avg `-0.061` n `142`; fx avg `0.0111` n `6`; index avg `-0.0266` n `26`; metal avg `-0.0115` n `20`; unknown avg `2.6462` n `969`
- 1h: commodity avg `-0.0065` n `12`; crypto_alt avg `0.5142` n `234`; crypto_major avg `0.5721` n `8`; equity avg `-0.0289` n `142`; fx avg `-0.0127` n `6`; index avg `-0.0268` n `26`; metal avg `0.0003` n `20`; unknown avg `2.3629` n `961`
- 4h: commodity avg `0.1683` n `12`; crypto_alt avg `-0.4733` n `234`; crypto_major avg `-0.5536` n `8`; equity avg `-0.3916` n `142`; fx avg `-0.0053` n `6`; index avg `-0.0216` n `26`; metal avg `-0.314` n `20`; unknown avg `4.7227` n `875`
- 24h: commodity avg `0.2017` n `12`; crypto_alt avg `1.0929` n `234`; crypto_major avg `0.9421` n `8`; equity avg `-0.121` n `142`; fx avg `0.0771` n `6`; index avg `0.1407` n `26`; metal avg `-0.0139` n `20`; unknown avg `15.7206` n `820`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
