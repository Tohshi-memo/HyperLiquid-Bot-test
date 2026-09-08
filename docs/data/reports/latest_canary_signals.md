# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T17:22:33.212404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0365` n `12`; crypto_alt avg `-0.4122` n `233`; crypto_major avg `-0.3808` n `8`; equity avg `-0.0268` n `134`; fx avg `0.0008` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0287` n `20`; unknown avg `0.8924` n `797`
- 1h: commodity avg `0.0037` n `12`; crypto_alt avg `-0.1565` n `233`; crypto_major avg `-0.0028` n `8`; equity avg `0.1901` n `134`; fx avg `-0.0086` n `6`; index avg `0.0181` n `26`; metal avg `0.0638` n `20`; unknown avg `0.4289` n `765`
- 4h: commodity avg `-0.3393` n `12`; crypto_alt avg `0.5962` n `232`; crypto_major avg `0.8548` n `8`; equity avg `0.8678` n `134`; fx avg `0.0095` n `6`; index avg `-0.0318` n `26`; metal avg `-0.099` n `20`; unknown avg `0.3784` n `759`
- 24h: commodity avg `-0.3044` n `12`; crypto_alt avg `0.4612` n `232`; crypto_major avg `0.118` n `8`; equity avg `1.0586` n `134`; fx avg `-0.068` n `6`; index avg `-0.0519` n `26`; metal avg `-0.0251` n `20`; unknown avg `7062.0056` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
