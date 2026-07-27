# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T12:03:07.945280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0724` n `12`; crypto_alt avg `0.0654` n `230`; crypto_major avg `0.0794` n `8`; equity avg `0.0801` n `100`; fx avg `-0.0042` n `6`; index avg `0.0105` n `25`; metal avg `0.0346` n `20`; unknown avg `0.0355` n `776`
- 1h: commodity avg `0.0346` n `12`; crypto_alt avg `-0.0296` n `230`; crypto_major avg `-0.1297` n `8`; equity avg `-0.1632` n `100`; fx avg `-0.004` n `6`; index avg `-0.0388` n `25`; metal avg `0.0017` n `20`; unknown avg `0.0511` n `776`
- 4h: commodity avg `-0.0822` n `12`; crypto_alt avg `-0.184` n `230`; crypto_major avg `-0.0536` n `8`; equity avg `-0.1581` n `100`; fx avg `-0.0313` n `6`; index avg `-0.0107` n `25`; metal avg `0.0429` n `20`; unknown avg `-0.0918` n `775`
- 24h: commodity avg `-0.5384` n `12`; crypto_alt avg `0.4311` n `230`; crypto_major avg `1.0543` n `8`; equity avg `0.9734` n `100`; fx avg `0.0812` n `6`; index avg `0.1064` n `25`; metal avg `0.3466` n `20`; unknown avg `-0.1098` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1992`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
