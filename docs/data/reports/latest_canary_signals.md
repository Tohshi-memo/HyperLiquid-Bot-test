# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T23:22:28.486956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.0707` n `239`; crypto_major avg `-0.108` n `8`; equity avg `-0.0033` n `162`; fx avg `-0.0018` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0113` n `20`; unknown avg `0.0973` n `1259`
- 1h: commodity avg `0.0167` n `13`; crypto_alt avg `0.1479` n `239`; crypto_major avg `0.1426` n `8`; equity avg `0.4775` n `162`; fx avg `0.0054` n `6`; index avg `0.0616` n `27`; metal avg `0.0222` n `20`; unknown avg `1.1402` n `1227`
- 4h: commodity avg `0.132` n `13`; crypto_alt avg `0.4548` n `239`; crypto_major avg `0.3267` n `8`; equity avg `0.4178` n `162`; fx avg `-0.0102` n `6`; index avg `0.0554` n `27`; metal avg `-0.0121` n `20`; unknown avg `162.3735` n `1189`
- 24h: commodity avg `0.9242` n `13`; crypto_alt avg `-0.0212` n `239`; crypto_major avg `-1.0954` n `8`; equity avg `-0.2084` n `162`; fx avg `-0.1245` n `6`; index avg `0.0597` n `27`; metal avg `-0.6309` n `20`; unknown avg `51.7216` n `1121`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
