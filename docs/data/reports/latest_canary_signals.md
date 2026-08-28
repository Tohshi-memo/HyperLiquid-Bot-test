# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T09:22:27.602190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0515` n `12`; crypto_alt avg `0.106` n `231`; crypto_major avg `-0.07` n `8`; equity avg `-0.0215` n `127`; fx avg `0.0035` n `6`; index avg `-0.0071` n `26`; metal avg `0.0109` n `20`; unknown avg `0.0475` n `792`
- 1h: commodity avg `0.0311` n `12`; crypto_alt avg `-0.1858` n `231`; crypto_major avg `-0.5279` n `8`; equity avg `-0.018` n `127`; fx avg `-0.0001` n `6`; index avg `0.0072` n `26`; metal avg `0.0549` n `20`; unknown avg `-0.0272` n `792`
- 4h: commodity avg `-0.0987` n `12`; crypto_alt avg `0.2276` n `231`; crypto_major avg `-0.1339` n `8`; equity avg `-0.1841` n `127`; fx avg `-0.051` n `6`; index avg `-0.0084` n `26`; metal avg `0.4332` n `20`; unknown avg `0.0174` n `760`
- 24h: commodity avg `0.2105` n `12`; crypto_alt avg `-1.4021` n `231`; crypto_major avg `-0.8851` n `8`; equity avg `-1.1683` n `127`; fx avg `-0.0744` n `6`; index avg `-0.0224` n `26`; metal avg `0.6305` n `20`; unknown avg `0.3299` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
