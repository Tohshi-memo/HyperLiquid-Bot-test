# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T12:08:23.812706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1505` n `12`; crypto_alt avg `-0.5391` n `228`; crypto_major avg `-0.4016` n `8`; equity avg `-0.0816` n `67`; fx avg `-0.0044` n `6`; index avg `-0.0728` n `23`; metal avg `-0.1606` n `18`; unknown avg `-0.0743` n `418`
- 1h: commodity avg `0.1963` n `12`; crypto_alt avg `-0.4168` n `228`; crypto_major avg `-0.4494` n `8`; equity avg `-0.0736` n `67`; fx avg `0.0016` n `6`; index avg `-0.0828` n `23`; metal avg `-0.2749` n `18`; unknown avg `-0.1626` n `418`
- 4h: commodity avg `0.3551` n `12`; crypto_alt avg `-0.7096` n `228`; crypto_major avg `-0.1985` n `8`; equity avg `0.4549` n `67`; fx avg `-0.0421` n `6`; index avg `0.2312` n `23`; metal avg `-0.6608` n `18`; unknown avg `-0.3288` n `418`
- 24h: commodity avg `-0.6369` n `12`; crypto_alt avg `-2.4753` n `228`; crypto_major avg `-1.2775` n `8`; equity avg `0.7193` n `67`; fx avg `-0.0447` n `6`; index avg `0.6947` n `23`; metal avg `-1.4673` n `18`; unknown avg `0.2479` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1947`, n `670`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1908`, n `670`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1754`, n `670`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1717`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1656`, n `670`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1485`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1351`, n `670`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1305`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1299`, n `670`, weak_sample_signal
