# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T12:22:32.839303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.8274` n `12`; crypto_alt avg `0.9584` n `228`; crypto_major avg `0.7534` n `8`; equity avg `0.212` n `67`; fx avg `-0.0028` n `6`; index avg `0.206` n `23`; metal avg `0.6982` n `18`; unknown avg `0.7738` n `418`
- 1h: commodity avg `-0.6787` n `12`; crypto_alt avg `0.4124` n `228`; crypto_major avg `0.3482` n `8`; equity avg `0.129` n `67`; fx avg `-0.0072` n `6`; index avg `0.133` n `23`; metal avg `0.5361` n `18`; unknown avg `0.68` n `418`
- 4h: commodity avg `-0.4612` n `12`; crypto_alt avg `0.1521` n `228`; crypto_major avg `0.3768` n `8`; equity avg `0.4248` n `67`; fx avg `-0.0486` n `6`; index avg `0.229` n `23`; metal avg `-0.06` n `18`; unknown avg `0.302` n `418`
- 24h: commodity avg `-1.4539` n `12`; crypto_alt avg `-1.5506` n `228`; crypto_major avg `-0.5345` n `8`; equity avg `0.929` n `67`; fx avg `-0.0474` n `6`; index avg `0.906` n `23`; metal avg `-0.7831` n `18`; unknown avg `0.9844` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.195`, n `670`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1905`, n `670`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1749`, n `670`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1718`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1654`, n `670`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1475`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1392`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1364`, n `670`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1318`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1306`, n `670`, weak_sample_signal
