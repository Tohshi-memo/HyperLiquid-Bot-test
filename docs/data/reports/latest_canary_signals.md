# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T19:52:33.087988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.0671` n `230`; crypto_major avg `-0.0126` n `8`; equity avg `-0.1443` n `113`; fx avg `-0.0071` n `6`; index avg `-0.0262` n `25`; metal avg `0.0148` n `20`; unknown avg `-0.0187` n `785`
- 1h: commodity avg `-0.0252` n `12`; crypto_alt avg `0.0672` n `230`; crypto_major avg `0.4252` n `8`; equity avg `-0.1545` n `113`; fx avg `-0.001` n `6`; index avg `-0.0227` n `25`; metal avg `0.097` n `20`; unknown avg `0.036` n `785`
- 4h: commodity avg `0.1201` n `12`; crypto_alt avg `-0.0392` n `230`; crypto_major avg `0.2531` n `8`; equity avg `-0.4012` n `113`; fx avg `0.0126` n `6`; index avg `-0.0487` n `25`; metal avg `0.2522` n `20`; unknown avg `-0.129` n `785`
- 24h: commodity avg `1.1755` n `12`; crypto_alt avg `-0.9624` n `230`; crypto_major avg `-0.9902` n `8`; equity avg `-1.5391` n `113`; fx avg `0.27` n `6`; index avg `-0.0966` n `25`; metal avg `0.199` n `20`; unknown avg `103.532` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
