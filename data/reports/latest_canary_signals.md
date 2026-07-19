# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T03:07:24.283900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `-0.0836` n `230`; crypto_major avg `-0.1217` n `8`; equity avg `-0.0059` n `96`; fx avg `-0.0005` n `6`; index avg `0.0259` n `25`; metal avg `0.0009` n `20`; unknown avg `0.2063` n `770`
- 1h: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.1971` n `230`; crypto_major avg `-0.192` n `8`; equity avg `-0.0525` n `96`; fx avg `-0.0094` n `6`; index avg `0.0405` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.1695` n `770`
- 4h: commodity avg `-0.1399` n `12`; crypto_alt avg `0.0779` n `230`; crypto_major avg `0.3024` n `8`; equity avg `0.2128` n `96`; fx avg `0.0473` n `6`; index avg `0.0137` n `25`; metal avg `0.0552` n `20`; unknown avg `-0.561` n `770`
- 24h: commodity avg `0.2491` n `12`; crypto_alt avg `-0.1169` n `230`; crypto_major avg `0.78` n `8`; equity avg `-0.2041` n `96`; fx avg `-0.0165` n `6`; index avg `0.0117` n `25`; metal avg `-0.0253` n `20`; unknown avg `0.0575` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
