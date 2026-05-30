# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T09:07:20.286885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0303` n `12`; crypto_alt avg `-0.0442` n `228`; crypto_major avg `-0.0304` n `8`; equity avg `0.0254` n `69`; fx avg `0.0227` n `6`; index avg `-0.0347` n `23`; metal avg `0.004` n `18`; unknown avg `0.1077` n `421`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.0852` n `228`; crypto_major avg `-0.0562` n `8`; equity avg `0.0394` n `69`; fx avg `0.0203` n `6`; index avg `-0.06` n `23`; metal avg `0.002` n `18`; unknown avg `-0.1522` n `421`
- 4h: commodity avg `-0.0464` n `12`; crypto_alt avg `-0.0962` n `228`; crypto_major avg `0.3282` n `8`; equity avg `0.1593` n `69`; fx avg `0.0271` n `6`; index avg `0.0539` n `23`; metal avg `-0.008` n `18`; unknown avg `-0.352` n `401`
- 24h: commodity avg `-0.5436` n `12`; crypto_alt avg `1.174` n `228`; crypto_major avg `1.7241` n `8`; equity avg `1.1296` n `69`; fx avg `0.1179` n `6`; index avg `0.1013` n `23`; metal avg `0.1634` n `18`; unknown avg `0.1006` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1927`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
