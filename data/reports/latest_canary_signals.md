# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T16:52:31.160416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0498` n `12`; crypto_alt avg `0.4266` n `233`; crypto_major avg `0.2835` n `8`; equity avg `0.2338` n `135`; fx avg `-0.0029` n `6`; index avg `0.0347` n `26`; metal avg `0.0023` n `20`; unknown avg `-0.0945` n `796`
- 1h: commodity avg `0.0576` n `12`; crypto_alt avg `-0.385` n `233`; crypto_major avg `-0.2088` n `8`; equity avg `-0.3393` n `135`; fx avg `0.0052` n `6`; index avg `-0.019` n `26`; metal avg `-0.0882` n `20`; unknown avg `-0.1029` n `788`
- 4h: commodity avg `0.2928` n `12`; crypto_alt avg `0.0428` n `233`; crypto_major avg `-0.1593` n `8`; equity avg `0.4301` n `135`; fx avg `0.0491` n `6`; index avg `-0.0258` n `26`; metal avg `-0.0801` n `20`; unknown avg `-0.4719` n `760`
- 24h: commodity avg `0.8052` n `12`; crypto_alt avg `-4.773` n `233`; crypto_major avg `-3.8387` n `8`; equity avg `-1.972` n `135`; fx avg `0.1166` n `6`; index avg `-0.2838` n `26`; metal avg `-1.1648` n `20`; unknown avg `-0.9212` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
