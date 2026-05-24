# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T03:07:19.109309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.0747` n `228`; crypto_major avg `0.1028` n `8`; equity avg `0.0527` n `67`; fx avg `-0.008` n `6`; index avg `-0.053` n `23`; metal avg `0.0237` n `18`; unknown avg `-0.2259` n `396`
- 1h: commodity avg `0.211` n `12`; crypto_alt avg `-0.0445` n `228`; crypto_major avg `0.092` n `8`; equity avg `-0.0231` n `67`; fx avg `-0.009` n `6`; index avg `0.0355` n `23`; metal avg `-0.04` n `18`; unknown avg `0.2008` n `396`
- 4h: commodity avg `0.3049` n `12`; crypto_alt avg `0.0305` n `228`; crypto_major avg `0.6421` n `8`; equity avg `0.3177` n `67`; fx avg `-0.0255` n `6`; index avg `0.4137` n `23`; metal avg `0.3216` n `18`; unknown avg `0.3105` n `396`
- 24h: commodity avg `-2.5318` n `12`; crypto_alt avg `1.9237` n `228`; crypto_major avg `2.4121` n `8`; equity avg `2.1322` n `67`; fx avg `0.0312` n `6`; index avg `1.167` n `23`; metal avg `1.1177` n `18`; unknown avg `1.6554` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
