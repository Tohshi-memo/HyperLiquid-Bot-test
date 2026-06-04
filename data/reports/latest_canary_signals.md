# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T20:52:21.509996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `-0.1779` n `228`; crypto_major avg `-0.1086` n `8`; equity avg `-0.0262` n `74`; fx avg `0.0075` n `6`; index avg `-0.0612` n `23`; metal avg `0.0174` n `18`; unknown avg `-0.0468` n `424`
- 1h: commodity avg `-0.0391` n `12`; crypto_alt avg `-0.6151` n `228`; crypto_major avg `-0.1511` n `8`; equity avg `-0.4331` n `74`; fx avg `0.0094` n `6`; index avg `-0.2098` n `23`; metal avg `-0.0866` n `18`; unknown avg `0.188` n `424`
- 4h: commodity avg `0.2709` n `12`; crypto_alt avg `-1.1454` n `228`; crypto_major avg `-0.6813` n `8`; equity avg `-0.7014` n `74`; fx avg `-0.0357` n `6`; index avg `-0.0838` n `23`; metal avg `-0.1096` n `18`; unknown avg `0.7266` n `424`
- 24h: commodity avg `-0.7688` n `12`; crypto_alt avg `-4.4572` n `228`; crypto_major avg `-2.6989` n `8`; equity avg `-0.6823` n `73`; fx avg `0.0171` n `6`; index avg `0.0397` n `23`; metal avg `1.0465` n `18`; unknown avg `0.1053` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
