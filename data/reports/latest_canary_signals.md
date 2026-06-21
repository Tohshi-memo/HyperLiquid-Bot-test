# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T00:37:31.475158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `12`; crypto_alt avg `-0.147` n `228`; crypto_major avg `-0.1156` n `8`; equity avg `-0.0481` n `78`; fx avg `0.002` n `6`; index avg `-0.0106` n `23`; metal avg `-0.0121` n `18`; unknown avg `-0.0758` n `701`
- 1h: commodity avg `0.021` n `12`; crypto_alt avg `-0.0488` n `228`; crypto_major avg `-0.2411` n `8`; equity avg `-0.0409` n `78`; fx avg `-0.0014` n `6`; index avg `-0.0182` n `23`; metal avg `-0.0269` n `18`; unknown avg `0.0644` n `701`
- 4h: commodity avg `0.1065` n `12`; crypto_alt avg `0.886` n `228`; crypto_major avg `0.68` n `8`; equity avg `0.1272` n `78`; fx avg `0.0024` n `6`; index avg `0.0057` n `23`; metal avg `0.0018` n `18`; unknown avg `0.1328` n `701`
- 24h: commodity avg `0.3656` n `12`; crypto_alt avg `0.5755` n `228`; crypto_major avg `1.1413` n `8`; equity avg `0.2964` n `78`; fx avg `0.0427` n `6`; index avg `-0.0022` n `23`; metal avg `-0.082` n `18`; unknown avg `-0.2854` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
