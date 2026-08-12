# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T06:52:27.732031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.0081` n `230`; crypto_major avg `-0.0101` n `8`; equity avg `0.0641` n `113`; fx avg `0.0059` n `6`; index avg `0.0094` n `25`; metal avg `0.1054` n `20`; unknown avg `-0.0255` n `786`
- 1h: commodity avg `-0.1302` n `12`; crypto_alt avg `-0.2407` n `230`; crypto_major avg `-0.223` n `8`; equity avg `0.0365` n `113`; fx avg `0.012` n `6`; index avg `0.009` n `25`; metal avg `0.1807` n `20`; unknown avg `-0.0256` n `770`
- 4h: commodity avg `-0.1063` n `12`; crypto_alt avg `-0.5447` n `230`; crypto_major avg `-0.2562` n `8`; equity avg `0.0193` n `113`; fx avg `0.0086` n `6`; index avg `0.0101` n `25`; metal avg `0.0662` n `20`; unknown avg `-0.046` n `770`
- 24h: commodity avg `-0.1195` n `12`; crypto_alt avg `-1.0471` n `230`; crypto_major avg `0.7481` n `8`; equity avg `2.0476` n `113`; fx avg `-0.0015` n `6`; index avg `0.2075` n `25`; metal avg `0.3009` n `20`; unknown avg `-0.0897` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.224`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2065`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
