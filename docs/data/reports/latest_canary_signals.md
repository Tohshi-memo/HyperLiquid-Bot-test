# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T16:07:32.168349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0417` n `12`; crypto_alt avg `-0.0653` n `232`; crypto_major avg `0.0947` n `8`; equity avg `0.0141` n `134`; fx avg `-0.0025` n `6`; index avg `0.0014` n `26`; metal avg `-0.0461` n `20`; unknown avg `2.479` n `795`
- 1h: commodity avg `-0.1674` n `12`; crypto_alt avg `0.4908` n `232`; crypto_major avg `0.5931` n `8`; equity avg `0.4076` n `134`; fx avg `-0.025` n `6`; index avg `0.0284` n `26`; metal avg `-0.098` n `20`; unknown avg `1.0538` n `795`
- 4h: commodity avg `-0.6426` n `12`; crypto_alt avg `1.1245` n `232`; crypto_major avg `1.2576` n `8`; equity avg `1.2251` n `134`; fx avg `-0.0056` n `6`; index avg `0.066` n `26`; metal avg `-0.0915` n `20`; unknown avg `0.6381` n `775`
- 24h: commodity avg `-0.3858` n `12`; crypto_alt avg `1.5409` n `232`; crypto_major avg `0.8787` n `8`; equity avg `1.2922` n `134`; fx avg `-0.0716` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0965` n `20`; unknown avg `7062.2687` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
