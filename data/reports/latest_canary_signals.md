# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T17:52:35.043370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `0.176` n `234`; crypto_major avg `0.1777` n `8`; equity avg `0.1259` n `142`; fx avg `0.0034` n `6`; index avg `0.0339` n `26`; metal avg `0.0006` n `20`; unknown avg `0.6332` n `969`
- 1h: commodity avg `-0.0171` n `12`; crypto_alt avg `-0.7576` n `234`; crypto_major avg `-0.5434` n `8`; equity avg `-0.143` n `142`; fx avg `-0.0002` n `6`; index avg `-0.0269` n `26`; metal avg `-0.0337` n `20`; unknown avg `3.4421` n `967`
- 4h: commodity avg `0.1139` n `12`; crypto_alt avg `-0.6174` n `234`; crypto_major avg `-0.282` n `8`; equity avg `-0.1286` n `142`; fx avg `0.02` n `6`; index avg `-0.008` n `26`; metal avg `-0.1471` n `20`; unknown avg `4.4097` n `875`
- 24h: commodity avg `0.1519` n `12`; crypto_alt avg `1.9987` n `234`; crypto_major avg `1.6098` n `8`; equity avg `0.0408` n `142`; fx avg `0.0791` n `6`; index avg `0.1408` n `26`; metal avg `-0.0165` n `20`; unknown avg `4.963` n `820`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
