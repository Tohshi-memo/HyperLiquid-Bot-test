# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T09:07:28.097344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.063` n `12`; crypto_alt avg `0.0043` n `233`; crypto_major avg `-0.0368` n `8`; equity avg `-0.0534` n `134`; fx avg `-0.0117` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0097` n `20`; unknown avg `0.0305` n `796`
- 1h: commodity avg `0.0455` n `12`; crypto_alt avg `0.1312` n `233`; crypto_major avg `-0.0332` n `8`; equity avg `-0.0363` n `134`; fx avg `0.0169` n `6`; index avg `-0.0319` n `26`; metal avg `-0.0844` n `20`; unknown avg `0.0257` n `790`
- 4h: commodity avg `0.2057` n `12`; crypto_alt avg `0.8474` n `233`; crypto_major avg `0.4915` n `8`; equity avg `0.1109` n `134`; fx avg `0.0252` n `6`; index avg `-0.0276` n `26`; metal avg `0.1339` n `20`; unknown avg `0.4933` n `772`
- 24h: commodity avg `-0.1349` n `12`; crypto_alt avg `0.961` n `232`; crypto_major avg `1.7294` n `8`; equity avg `1.5514` n `134`; fx avg `-0.0988` n `6`; index avg `0.0673` n `26`; metal avg `0.0501` n `20`; unknown avg `0.97` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
