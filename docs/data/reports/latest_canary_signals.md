# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T18:37:28.809496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0389` n `12`; crypto_alt avg `-0.1441` n `230`; crypto_major avg `-0.1572` n `8`; equity avg `-0.322` n `100`; fx avg `0.0009` n `6`; index avg `-0.0739` n `25`; metal avg `-0.0162` n `20`; unknown avg `0.0339` n `773`
- 1h: commodity avg `-0.031` n `12`; crypto_alt avg `-0.3696` n `230`; crypto_major avg `-0.2945` n `8`; equity avg `-0.9496` n `100`; fx avg `0.0018` n `6`; index avg `-0.166` n `25`; metal avg `-0.1277` n `20`; unknown avg `-0.0678` n `773`
- 4h: commodity avg `-0.2844` n `12`; crypto_alt avg `0.318` n `230`; crypto_major avg `0.1907` n `8`; equity avg `-0.227` n `100`; fx avg `-0.0124` n `6`; index avg `-0.0324` n `25`; metal avg `0.0108` n `20`; unknown avg `13.3627` n `773`
- 24h: commodity avg `-0.6061` n `12`; crypto_alt avg `-1.152` n `230`; crypto_major avg `-1.0864` n `8`; equity avg `-3.0243` n `100`; fx avg `-0.1565` n `6`; index avg `-0.3764` n `25`; metal avg `0.0595` n `20`; unknown avg `14.1463` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1233`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1189`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1098`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1062`, n `666`, weak_sample_signal
