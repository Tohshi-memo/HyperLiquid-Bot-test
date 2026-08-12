# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T16:37:25.953995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `-0.0408` n `230`; crypto_major avg `0.0509` n `8`; equity avg `-0.0752` n `113`; fx avg `0.0015` n `6`; index avg `-0.0256` n `25`; metal avg `-0.063` n `20`; unknown avg `-0.0687` n `786`
- 1h: commodity avg `-0.0572` n `12`; crypto_alt avg `-0.0144` n `230`; crypto_major avg `-0.0436` n `8`; equity avg `0.2491` n `113`; fx avg `-0.0115` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0519` n `20`; unknown avg `-0.0366` n `786`
- 4h: commodity avg `-0.1265` n `12`; crypto_alt avg `-0.7539` n `230`; crypto_major avg `-0.6551` n `8`; equity avg `0.6162` n `113`; fx avg `-0.0075` n `6`; index avg `0.032` n `25`; metal avg `-0.2521` n `20`; unknown avg `0.0949` n `786`
- 24h: commodity avg `0.1272` n `12`; crypto_alt avg `-0.1377` n `230`; crypto_major avg `1.055` n `8`; equity avg `3.5407` n `113`; fx avg `0.0471` n `6`; index avg `0.3252` n `25`; metal avg `0.201` n `20`; unknown avg `0.0101` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2268`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2019`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
