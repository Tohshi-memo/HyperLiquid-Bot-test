# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T05:22:20.325999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `-0.2603` n `228`; crypto_major avg `-0.0948` n `8`; equity avg `-0.0196` n `67`; fx avg `0.005` n `6`; index avg `-0.0008` n `23`; metal avg `-0.0083` n `18`; unknown avg `0.0425` n `386`
- 1h: commodity avg `0.0175` n `12`; crypto_alt avg `-0.357` n `228`; crypto_major avg `-0.265` n `8`; equity avg `-0.1222` n `67`; fx avg `0.0061` n `6`; index avg `-0.0834` n `23`; metal avg `-0.0354` n `18`; unknown avg `-0.2348` n `386`
- 4h: commodity avg `0.145` n `12`; crypto_alt avg `-0.1171` n `228`; crypto_major avg `-0.0908` n `8`; equity avg `-0.0103` n `67`; fx avg `0.0036` n `6`; index avg `-0.0098` n `23`; metal avg `0.0393` n `18`; unknown avg `-0.8947` n `386`
- 24h: commodity avg `0.0824` n `12`; crypto_alt avg `-4.3865` n `228`; crypto_major avg `-2.8427` n `8`; equity avg `-2.0939` n `67`; fx avg `0.0493` n `6`; index avg `-0.1535` n `23`; metal avg `-0.946` n `18`; unknown avg `-2.352` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
