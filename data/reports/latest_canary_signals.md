# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T01:22:26.873864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `12`; crypto_alt avg `0.0023` n `230`; crypto_major avg `-0.0297` n `8`; equity avg `-0.0562` n `113`; fx avg `-0.0003` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0871` n `20`; unknown avg `-0.0673` n `786`
- 1h: commodity avg `-0.0772` n `12`; crypto_alt avg `-0.2059` n `230`; crypto_major avg `-0.1214` n `8`; equity avg `-0.1545` n `113`; fx avg `-0.0074` n `6`; index avg `-0.0629` n `25`; metal avg `-0.1136` n `20`; unknown avg `-0.14` n `786`
- 4h: commodity avg `-0.1557` n `12`; crypto_alt avg `-0.2958` n `230`; crypto_major avg `-0.2195` n `8`; equity avg `0.2326` n `113`; fx avg `-0.0438` n `6`; index avg `0.0318` n `25`; metal avg `0.062` n `20`; unknown avg `-0.1731` n `786`
- 24h: commodity avg `-0.2434` n `12`; crypto_alt avg `-1.3205` n `230`; crypto_major avg `-0.5058` n `8`; equity avg `2.8627` n `113`; fx avg `-0.0376` n `6`; index avg `0.3964` n `25`; metal avg `0.0989` n `20`; unknown avg `0.0194` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2389`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2036`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
