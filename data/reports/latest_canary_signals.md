# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T03:22:24.785915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `0.0964` n `231`; crypto_major avg `-0.0245` n `8`; equity avg `-0.009` n `128`; fx avg `0.0006` n `6`; index avg `-0.0189` n `26`; metal avg `0.0008` n `20`; unknown avg `-0.0475` n `793`
- 1h: commodity avg `-0.0037` n `12`; crypto_alt avg `0.2188` n `231`; crypto_major avg `-0.0664` n `8`; equity avg `-0.0258` n `128`; fx avg `0.006` n `6`; index avg `-0.0025` n `26`; metal avg `-0.0045` n `20`; unknown avg `0.1089` n `793`
- 4h: commodity avg `-0.0064` n `12`; crypto_alt avg `0.0279` n `231`; crypto_major avg `-0.1722` n `8`; equity avg `0.0147` n `128`; fx avg `0.0177` n `6`; index avg `-0.0147` n `26`; metal avg `-0.013` n `20`; unknown avg `3.6325` n `793`
- 24h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.2716` n `231`; crypto_major avg `0.6407` n `8`; equity avg `0.3275` n `128`; fx avg `-0.003` n `6`; index avg `0.0575` n `26`; metal avg `0.1038` n `20`; unknown avg `0.0845` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2039`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
