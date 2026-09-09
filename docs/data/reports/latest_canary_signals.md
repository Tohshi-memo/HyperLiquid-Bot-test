# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T05:37:27.636719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `-0.1749` n `233`; crypto_major avg `-0.1871` n `8`; equity avg `0.0027` n `134`; fx avg `-0.0113` n `6`; index avg `0.0128` n `26`; metal avg `0.0461` n `20`; unknown avg `0.5885` n `798`
- 1h: commodity avg `-0.0478` n `12`; crypto_alt avg `0.1665` n `233`; crypto_major avg `0.0082` n `8`; equity avg `-0.1225` n `134`; fx avg `-0.0071` n `6`; index avg `-0.029` n `26`; metal avg `0.0976` n `20`; unknown avg `0.2049` n `796`
- 4h: commodity avg `-0.1549` n `12`; crypto_alt avg `0.4707` n `233`; crypto_major avg `0.2944` n `8`; equity avg `-0.2887` n `134`; fx avg `-0.0611` n `6`; index avg `-0.0555` n `26`; metal avg `0.0609` n `20`; unknown avg `0.3007` n `785`
- 24h: commodity avg `-0.1393` n `12`; crypto_alt avg `-0.1354` n `232`; crypto_major avg `0.9326` n `8`; equity avg `0.4478` n `134`; fx avg `-0.0804` n `6`; index avg `-0.1206` n `26`; metal avg `-0.2233` n `20`; unknown avg `0.3957` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
