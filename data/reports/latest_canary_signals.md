# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T21:52:18.419689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.0046` n `228`; crypto_major avg `-0.0605` n `8`; equity avg `-0.0997` n `69`; fx avg `-0.0019` n `6`; index avg `0.0735` n `23`; metal avg `0.0047` n `18`; unknown avg `0.262` n `419`
- 1h: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.2944` n `228`; crypto_major avg `-0.366` n `8`; equity avg `-0.0637` n `69`; fx avg `-0.0172` n `6`; index avg `-0.0029` n `23`; metal avg `-0.0266` n `18`; unknown avg `0.4107` n `419`
- 4h: commodity avg `0.1707` n `12`; crypto_alt avg `-0.9923` n `228`; crypto_major avg `-0.892` n `8`; equity avg `0.0499` n `69`; fx avg `-0.0194` n `6`; index avg `0.0594` n `23`; metal avg `-0.0892` n `18`; unknown avg `-0.1831` n `419`
- 24h: commodity avg `-0.542` n `12`; crypto_alt avg `-0.0134` n `228`; crypto_major avg `0.2241` n `8`; equity avg `1.0801` n `69`; fx avg `0.1833` n `6`; index avg `0.1839` n `23`; metal avg `0.0111` n `18`; unknown avg `0.4072` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
