# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T04:45:03.691028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `0.0325` n `228`; crypto_major avg `0.0368` n `8`; equity avg `0.0464` n `67`; fx avg `0.0222` n `6`; index avg `-0.0212` n `23`; metal avg `0.0093` n `18`; unknown avg `-0.1427` n `396`
- 1h: commodity avg `-0.0616` n `12`; crypto_alt avg `0.1855` n `228`; crypto_major avg `0.0004` n `8`; equity avg `0.1357` n `67`; fx avg `0.033` n `6`; index avg `-0.0191` n `23`; metal avg `-0.0313` n `18`; unknown avg `-0.3374` n `396`
- 4h: commodity avg `-0.132` n `12`; crypto_alt avg `-0.327` n `228`; crypto_major avg `0.0949` n `8`; equity avg `0.2169` n `67`; fx avg `0.0183` n `6`; index avg `0.1529` n `23`; metal avg `0.1786` n `18`; unknown avg `-0.5919` n `396`
- 24h: commodity avg `-2.893` n `12`; crypto_alt avg `1.9271` n `228`; crypto_major avg `2.4607` n `8`; equity avg `2.3277` n `67`; fx avg `0.07` n `6`; index avg `1.1456` n `23`; metal avg `1.2012` n `18`; unknown avg `1.8393` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
