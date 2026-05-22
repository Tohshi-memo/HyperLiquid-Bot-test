# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T11:37:15.622089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0299` n `12`; crypto_alt avg `0.2275` n `228`; crypto_major avg `0.1004` n `8`; equity avg `0.0847` n `67`; fx avg `-0.0008` n `6`; index avg `0.0233` n `23`; metal avg `0.0677` n `18`; unknown avg `0.015` n `386`
- 1h: commodity avg `-0.0171` n `12`; crypto_alt avg `0.064` n `228`; crypto_major avg `0.0473` n `8`; equity avg `0.1752` n `67`; fx avg `-0.009` n `6`; index avg `0.0534` n `23`; metal avg `-0.0889` n `18`; unknown avg `-0.0789` n `386`
- 4h: commodity avg `-0.1103` n `12`; crypto_alt avg `0.0048` n `228`; crypto_major avg `0.2824` n `8`; equity avg `-0.4629` n `67`; fx avg `-0.0021` n `6`; index avg `-0.1335` n `23`; metal avg `0.2119` n `18`; unknown avg `-0.0828` n `386`
- 24h: commodity avg `-0.9043` n `12`; crypto_alt avg `2.6645` n `228`; crypto_major avg `1.1234` n `8`; equity avg `1.1886` n `67`; fx avg `0.0767` n `6`; index avg `0.7557` n `23`; metal avg `1.0362` n `18`; unknown avg `1.1264` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0383`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0367`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0354`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0318`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0311`, n `668`, weak_sample_signal
