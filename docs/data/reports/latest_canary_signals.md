# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T03:37:20.979805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1957` n `12`; crypto_alt avg `-0.1376` n `228`; crypto_major avg `-0.0448` n `8`; equity avg `0.0245` n `67`; fx avg `0.0006` n `6`; index avg `-0.0043` n `23`; metal avg `0.0045` n `18`; unknown avg `0.172` n `396`
- 1h: commodity avg `-0.2014` n `12`; crypto_alt avg `0.0002` n `228`; crypto_major avg `0.1975` n `8`; equity avg `0.0542` n `67`; fx avg `-0.0023` n `6`; index avg `0.0169` n `23`; metal avg `0.105` n `18`; unknown avg `0.0013` n `396`
- 4h: commodity avg `0.097` n `12`; crypto_alt avg `-0.3943` n `228`; crypto_major avg `0.4198` n `8`; equity avg `0.2566` n `67`; fx avg `-0.0259` n `6`; index avg `0.3152` n `23`; metal avg `0.3436` n `18`; unknown avg `0.5042` n `396`
- 24h: commodity avg `-2.9671` n `12`; crypto_alt avg `1.2216` n `228`; crypto_major avg `2.1968` n `8`; equity avg `2.184` n `67`; fx avg `0.0364` n `6`; index avg `1.1653` n `23`; metal avg `1.2207` n `18`; unknown avg `1.8229` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
