# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T01:37:23.920606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `12`; crypto_alt avg `0.0201` n `230`; crypto_major avg `-0.0217` n `8`; equity avg `0.0785` n `113`; fx avg `0.0149` n `6`; index avg `0.03` n `25`; metal avg `-0.0376` n `20`; unknown avg `-0.0122` n `786`
- 1h: commodity avg `0.041` n `12`; crypto_alt avg `0.0968` n `230`; crypto_major avg `0.032` n `8`; equity avg `0.0744` n `113`; fx avg `0.0099` n `6`; index avg `0.0233` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0864` n `786`
- 4h: commodity avg `0.1283` n `12`; crypto_alt avg `0.1811` n `230`; crypto_major avg `0.1538` n `8`; equity avg `0.3771` n `113`; fx avg `0.0257` n `6`; index avg `0.0399` n `25`; metal avg `0.0847` n `20`; unknown avg `-0.1151` n `786`
- 24h: commodity avg `0.2168` n `12`; crypto_alt avg `-1.2155` n `230`; crypto_major avg `0.6818` n `8`; equity avg `1.2938` n `113`; fx avg `0.0083` n `6`; index avg `0.0948` n `25`; metal avg `-0.3201` n `20`; unknown avg `-0.0977` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2279`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2221`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.205`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2026`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
