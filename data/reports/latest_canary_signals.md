# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T22:06:19.170181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0345` n `12`; crypto_alt avg `-0.194` n `228`; crypto_major avg `-0.169` n `8`; equity avg `-0.0079` n `67`; fx avg `0.0022` n `6`; index avg `-0.0035` n `23`; metal avg `0.0039` n `18`; unknown avg `-0.0857` n `386`
- 1h: commodity avg `0.0891` n `12`; crypto_alt avg `0.0562` n `228`; crypto_major avg `0.2343` n `8`; equity avg `-0.0198` n `67`; fx avg `-0.0024` n `6`; index avg `-0.0649` n `23`; metal avg `0.0398` n `18`; unknown avg `-0.3353` n `386`
- 4h: commodity avg `0.4493` n `12`; crypto_alt avg `-1.9844` n `228`; crypto_major avg `-1.3752` n `8`; equity avg `-0.8909` n `67`; fx avg `0.0302` n `6`; index avg `-0.3939` n `23`; metal avg `-0.222` n `18`; unknown avg `1.5002` n `386`
- 24h: commodity avg `-0.4896` n `12`; crypto_alt avg `-2.8051` n `228`; crypto_major avg `-2.0178` n `8`; equity avg `-1.168` n `67`; fx avg `0.1863` n `6`; index avg `0.3698` n `23`; metal avg `-1.008` n `18`; unknown avg `-1.358` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
