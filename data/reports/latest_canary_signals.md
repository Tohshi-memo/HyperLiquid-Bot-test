# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T06:23:06.934081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0445` n `12`; crypto_alt avg `0.4862` n `233`; crypto_major avg `0.4609` n `8`; equity avg `0.112` n `134`; fx avg `-0.0001` n `6`; index avg `0.0008` n `26`; metal avg `-0.0104` n `20`; unknown avg `0.6426` n `798`
- 1h: commodity avg `0.0339` n `12`; crypto_alt avg `0.2102` n `233`; crypto_major avg `0.2488` n `8`; equity avg `0.2282` n `134`; fx avg `-0.0224` n `6`; index avg `0.0357` n `26`; metal avg `0.1238` n `20`; unknown avg `0.6889` n `778`
- 4h: commodity avg `-0.0738` n `12`; crypto_alt avg `1.1037` n `233`; crypto_major avg `0.8367` n `8`; equity avg `0.0298` n `134`; fx avg `-0.0858` n `6`; index avg `-0.0158` n `26`; metal avg `0.1864` n `20`; unknown avg `0.4491` n `769`
- 24h: commodity avg `-0.151` n `12`; crypto_alt avg `0.6929` n `232`; crypto_major avg `1.7593` n `8`; equity avg `1.3667` n `134`; fx avg `-0.1347` n `6`; index avg `0.0418` n `26`; metal avg `-0.01` n `20`; unknown avg `0.3577` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
