# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T08:52:24.078388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.091` n `12`; crypto_alt avg `-0.3153` n `231`; crypto_major avg `-0.2972` n `8`; equity avg `-0.0556` n `127`; fx avg `0.0035` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0298` n `20`; unknown avg `-0.0311` n `792`
- 1h: commodity avg `0.0328` n `12`; crypto_alt avg `-0.2995` n `231`; crypto_major avg `-0.2228` n `8`; equity avg `-0.0518` n `127`; fx avg `-0.0017` n `6`; index avg `-0.0138` n `26`; metal avg `-0.0005` n `20`; unknown avg `-0.0516` n `792`
- 4h: commodity avg `-0.1201` n `12`; crypto_alt avg `-0.3065` n `231`; crypto_major avg `-0.1511` n `8`; equity avg `-0.3549` n `127`; fx avg `-0.0608` n `6`; index avg `-0.0347` n `26`; metal avg `0.3553` n `20`; unknown avg `0.0466` n `760`
- 24h: commodity avg `0.3106` n `12`; crypto_alt avg `-1.442` n `231`; crypto_major avg `-0.3562` n `8`; equity avg `-1.2099` n `127`; fx avg `-0.0804` n `6`; index avg `-0.0503` n `26`; metal avg `0.5358` n `20`; unknown avg `0.3715` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
