# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T02:07:29.103192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `0.2954` n `230`; crypto_major avg `0.3137` n `8`; equity avg `0.0515` n `96`; fx avg `0.0147` n `6`; index avg `-0.0079` n `25`; metal avg `0.0084` n `20`; unknown avg `0.1786` n `770`
- 1h: commodity avg `-0.0147` n `12`; crypto_alt avg `0.3178` n `230`; crypto_major avg `0.3902` n `8`; equity avg `0.1015` n `96`; fx avg `0.0196` n `6`; index avg `-0.0146` n `25`; metal avg `0.0261` n `20`; unknown avg `0.21` n `770`
- 4h: commodity avg `-0.0352` n `12`; crypto_alt avg `0.2745` n `230`; crypto_major avg `0.4084` n `8`; equity avg `0.191` n `96`; fx avg `0.0562` n `6`; index avg `-0.0134` n `25`; metal avg `0.045` n `20`; unknown avg `-0.5709` n `770`
- 24h: commodity avg `0.2883` n `12`; crypto_alt avg `0.2425` n `230`; crypto_major avg `1.094` n `8`; equity avg `-0.1009` n `96`; fx avg `-0.0164` n `6`; index avg `-0.019` n `25`; metal avg `-0.0327` n `20`; unknown avg `0.0941` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
