# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T07:52:25.507670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.059` n `12`; crypto_alt avg `0.0323` n `233`; crypto_major avg `-0.0021` n `8`; equity avg `-0.0691` n `134`; fx avg `-0.0116` n `6`; index avg `-0.0229` n `26`; metal avg `0.0052` n `20`; unknown avg `0.159` n `798`
- 1h: commodity avg `0.0597` n `12`; crypto_alt avg `0.18` n `233`; crypto_major avg `0.1774` n `8`; equity avg `-0.0308` n `134`; fx avg `-0.0213` n `6`; index avg `-0.0145` n `26`; metal avg `0.0941` n `20`; unknown avg `0.4473` n `796`
- 4h: commodity avg `0.0753` n `12`; crypto_alt avg `1.532` n `233`; crypto_major avg `1.1146` n `8`; equity avg `0.2156` n `134`; fx avg `-0.0402` n `6`; index avg `0.0089` n `26`; metal avg `0.2825` n `20`; unknown avg `1.3762` n `771`
- 24h: commodity avg `-0.1852` n `11`; crypto_alt avg `0.8016` n `232`; crypto_major avg `1.7234` n `8`; equity avg `1.339` n `123`; fx avg `-0.1185` n `5`; index avg `0.0883` n `20`; metal avg `0.1714` n `18`; unknown avg `0.3753` n `687`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
