# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T05:22:26.156988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `-0.0483` n `231`; crypto_major avg `-0.0553` n `8`; equity avg `0.0046` n `128`; fx avg `0.0005` n `6`; index avg `0.015` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.0615` n `793`
- 1h: commodity avg `0.007` n `12`; crypto_alt avg `0.0577` n `231`; crypto_major avg `0.0234` n `8`; equity avg `-0.0005` n `128`; fx avg `-0.0013` n `6`; index avg `0.0241` n `26`; metal avg `-0.0001` n `20`; unknown avg `-0.2961` n `793`
- 4h: commodity avg `0.0036` n `12`; crypto_alt avg `0.2622` n `231`; crypto_major avg `-0.0004` n `8`; equity avg `0.0344` n `128`; fx avg `0.0051` n `6`; index avg `0.0211` n `26`; metal avg `-0.0017` n `20`; unknown avg `-0.6545` n `793`
- 24h: commodity avg `0.0118` n `12`; crypto_alt avg `0.1909` n `231`; crypto_major avg `0.5285` n `8`; equity avg `0.3015` n `128`; fx avg `-0.0159` n `6`; index avg `0.0621` n `26`; metal avg `0.0818` n `20`; unknown avg `0.0541` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
