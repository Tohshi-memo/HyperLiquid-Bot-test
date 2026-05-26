# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T13:52:21.701501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3893` n `12`; crypto_alt avg `0.5323` n `228`; crypto_major avg `0.5896` n `8`; equity avg `0.1628` n `67`; fx avg `-0.0199` n `6`; index avg `0.1298` n `23`; metal avg `-0.274` n `18`; unknown avg `0.2014` n `418`
- 1h: commodity avg `0.6838` n `12`; crypto_alt avg `0.3181` n `228`; crypto_major avg `0.4758` n `8`; equity avg `-0.0916` n `67`; fx avg `-0.0201` n `6`; index avg `0.343` n `23`; metal avg `0.0705` n `18`; unknown avg `0.3087` n `418`
- 4h: commodity avg `0.3441` n `12`; crypto_alt avg `1.59` n `228`; crypto_major avg `1.7339` n `8`; equity avg `0.2457` n `67`; fx avg `-0.0577` n `6`; index avg `0.5305` n `23`; metal avg `0.2986` n `18`; unknown avg `1.1326` n `417`
- 24h: commodity avg `0.8369` n `12`; crypto_alt avg `0.4241` n `228`; crypto_major avg `-0.1069` n `8`; equity avg `-0.3787` n `67`; fx avg `-0.1526` n `6`; index avg `0.4158` n `23`; metal avg `-0.521` n `18`; unknown avg `-0.1777` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
