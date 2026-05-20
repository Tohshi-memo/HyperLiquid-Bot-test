# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T11:22:17.795194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2906` n `12`; crypto_alt avg `-0.0293` n `228`; crypto_major avg `-0.0965` n `8`; equity avg `0.0041` n `66`; fx avg `-0.0197` n `6`; index avg `0.0181` n `23`; metal avg `-0.1062` n `18`; unknown avg `-0.0278` n `384`
- 1h: commodity avg `0.0673` n `12`; crypto_alt avg `-0.0783` n `228`; crypto_major avg `-0.0007` n `8`; equity avg `0.0101` n `66`; fx avg `0.0088` n `6`; index avg `0.0166` n `23`; metal avg `0.0561` n `18`; unknown avg `0.3238` n `384`
- 4h: commodity avg `-0.1752` n `12`; crypto_alt avg `-0.0858` n `228`; crypto_major avg `0.3015` n `8`; equity avg `0.3084` n `66`; fx avg `0.0029` n `6`; index avg `0.2624` n `23`; metal avg `0.2666` n `18`; unknown avg `0.0002` n `384`
- 24h: commodity avg `-0.2511` n `12`; crypto_alt avg `0.9009` n `228`; crypto_major avg `0.6828` n `8`; equity avg `1.5465` n `66`; fx avg `-0.099` n `6`; index avg `0.2098` n `23`; metal avg `-0.7584` n `18`; unknown avg `0.7263` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
