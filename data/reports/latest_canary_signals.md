# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T17:37:20.284157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0458` n `12`; crypto_alt avg `-0.0366` n `228`; crypto_major avg `-0.0604` n `8`; equity avg `0.1188` n `67`; fx avg `-0.0036` n `6`; index avg `0.0125` n `23`; metal avg `0.016` n `18`; unknown avg `0.0841` n `396`
- 1h: commodity avg `0.1204` n `12`; crypto_alt avg `0.2765` n `228`; crypto_major avg `0.0097` n `8`; equity avg `0.0554` n `67`; fx avg `-0.0051` n `6`; index avg `0.0312` n `23`; metal avg `0.045` n `18`; unknown avg `0.0186` n `396`
- 4h: commodity avg `-0.626` n `12`; crypto_alt avg `1.7654` n `228`; crypto_major avg `1.1526` n `8`; equity avg `0.6409` n `67`; fx avg `0.0047` n `6`; index avg `0.1675` n `23`; metal avg `0.2179` n `18`; unknown avg `0.8371` n `396`
- 24h: commodity avg `0.6256` n `12`; crypto_alt avg `-2.9823` n `228`; crypto_major avg `-2.1622` n `8`; equity avg `-1.0068` n `67`; fx avg `0.0136` n `6`; index avg `-0.3387` n `23`; metal avg `-0.2159` n `18`; unknown avg `-1.5315` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
