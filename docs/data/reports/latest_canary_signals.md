# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T10:03:33.846218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0342` n `12`; crypto_alt avg `0.0181` n `228`; crypto_major avg `0.068` n `8`; equity avg `0.0445` n `66`; fx avg `0.0017` n `6`; index avg `-0.0503` n `23`; metal avg `-0.0342` n `18`; unknown avg `-0.0976` n `384`
- 1h: commodity avg `0.2337` n `12`; crypto_alt avg `0.078` n `228`; crypto_major avg `0.209` n `8`; equity avg `0.1634` n `66`; fx avg `0.018` n `6`; index avg `0.0388` n `23`; metal avg `0.0332` n `18`; unknown avg `0.3567` n `384`
- 4h: commodity avg `-0.5311` n `12`; crypto_alt avg `0.1542` n `228`; crypto_major avg `0.3919` n `8`; equity avg `0.7307` n `66`; fx avg `-0.0587` n `6`; index avg `0.3844` n `23`; metal avg `0.6679` n `18`; unknown avg `0.3843` n `384`
- 24h: commodity avg `0.0244` n `12`; crypto_alt avg `0.5035` n `228`; crypto_major avg `0.5113` n `8`; equity avg `1.3923` n `66`; fx avg `-0.1553` n `6`; index avg `0.2039` n `23`; metal avg `-0.8262` n `18`; unknown avg `0.9901` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
