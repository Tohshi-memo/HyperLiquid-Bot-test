# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T18:37:29.172395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `-0.3136` n `233`; crypto_major avg `-0.2976` n `8`; equity avg `-0.1024` n `134`; fx avg `-0.0198` n `6`; index avg `-0.0107` n `26`; metal avg `-0.0364` n `20`; unknown avg `0.865` n `797`
- 1h: commodity avg `0.2521` n `12`; crypto_alt avg `-0.2448` n `233`; crypto_major avg `0.0234` n `8`; equity avg `-0.1256` n `134`; fx avg `-0.0303` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0597` n `20`; unknown avg `3.6854` n `795`
- 4h: commodity avg `0.0599` n `12`; crypto_alt avg `0.2531` n `232`; crypto_major avg `0.7575` n `8`; equity avg `0.6333` n `134`; fx avg `-0.013` n `6`; index avg `0.0774` n `26`; metal avg `-0.064` n `20`; unknown avg `0.3817` n `765`
- 24h: commodity avg `-0.0874` n `12`; crypto_alt avg `0.6242` n `232`; crypto_major avg `0.5374` n `8`; equity avg `0.9122` n `134`; fx avg `-0.0771` n `6`; index avg `-0.0452` n `26`; metal avg `-0.0781` n `20`; unknown avg `9.1775` n `706`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
