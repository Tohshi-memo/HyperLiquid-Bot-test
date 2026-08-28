# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T11:22:24.434506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0321` n `12`; crypto_alt avg `-0.0186` n `231`; crypto_major avg `-0.0073` n `8`; equity avg `0.0278` n `127`; fx avg `-0.0035` n `6`; index avg `0.0105` n `26`; metal avg `0.0125` n `20`; unknown avg `-0.0541` n `792`
- 1h: commodity avg `-0.0582` n `12`; crypto_alt avg `0.7899` n `231`; crypto_major avg `0.7947` n `8`; equity avg `0.1251` n `127`; fx avg `0.0563` n `6`; index avg `0.0103` n `26`; metal avg `0.0003` n `20`; unknown avg `0.0742` n `792`
- 4h: commodity avg `-0.0284` n `12`; crypto_alt avg `0.3436` n `231`; crypto_major avg `-0.0404` n `8`; equity avg `-0.0367` n `127`; fx avg `0.0652` n `6`; index avg `-0.0104` n `26`; metal avg `0.1595` n `20`; unknown avg `-0.0465` n `792`
- 24h: commodity avg `0.0838` n `12`; crypto_alt avg `-0.1657` n `231`; crypto_major avg `0.1047` n `8`; equity avg `-0.9118` n `127`; fx avg `-0.0209` n `6`; index avg `-0.0271` n `26`; metal avg `0.6773` n `20`; unknown avg `0.3302` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
