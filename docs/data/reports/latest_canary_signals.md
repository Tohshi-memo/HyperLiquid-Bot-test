# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T06:37:14.657798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `0.313` n `228`; crypto_major avg `0.2536` n `8`; equity avg `0.0489` n `67`; fx avg `0.0011` n `6`; index avg `-0.0145` n `23`; metal avg `-0.0716` n `18`; unknown avg `-0.1662` n `418`
- 1h: commodity avg `0.0289` n `12`; crypto_alt avg `0.3669` n `228`; crypto_major avg `0.1906` n `8`; equity avg `-0.0988` n `67`; fx avg `0.0195` n `6`; index avg `-0.1178` n `23`; metal avg `-0.6216` n `18`; unknown avg `0.0279` n `400`
- 4h: commodity avg `-0.3481` n `12`; crypto_alt avg `0.4259` n `228`; crypto_major avg `0.6025` n `8`; equity avg `-0.3568` n `67`; fx avg `0.0092` n `6`; index avg `-0.3502` n `23`; metal avg `-0.8224` n `18`; unknown avg `0.0111` n `400`
- 24h: commodity avg `-0.3225` n `12`; crypto_alt avg `-0.9372` n `228`; crypto_major avg `-0.3421` n `8`; equity avg `0.3032` n `67`; fx avg `-0.02` n `6`; index avg `0.6869` n `23`; metal avg `-0.9487` n `18`; unknown avg `0.6606` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
