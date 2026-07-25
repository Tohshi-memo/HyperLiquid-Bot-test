# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T11:59:19.252166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0388` n `12`; crypto_alt avg `0.0408` n `230`; crypto_major avg `0.0668` n `8`; equity avg `0.0635` n `100`; fx avg `-0.003` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0047` n `20`; unknown avg `-0.0031` n `774`
- 1h: commodity avg `-0.0558` n `12`; crypto_alt avg `-0.076` n `230`; crypto_major avg `0.0101` n `8`; equity avg `-0.0193` n `100`; fx avg `-0.0095` n `6`; index avg `-0.0107` n `25`; metal avg `0.0009` n `20`; unknown avg `-0.0835` n `774`
- 4h: commodity avg `-0.075` n `12`; crypto_alt avg `-0.0571` n `230`; crypto_major avg `0.1947` n `8`; equity avg `-0.0503` n `100`; fx avg `-0.0163` n `6`; index avg `0.0052` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.5893` n `774`
- 24h: commodity avg `-0.1625` n `12`; crypto_alt avg `-1.2406` n `230`; crypto_major avg `-0.8488` n `8`; equity avg `-2.8026` n `100`; fx avg `-0.0106` n `6`; index avg `-0.236` n `25`; metal avg `-0.0886` n `20`; unknown avg `13.1267` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1174`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1014`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
