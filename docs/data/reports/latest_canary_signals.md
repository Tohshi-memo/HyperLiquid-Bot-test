# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T12:52:29.734902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.3066` n `234`; crypto_major avg `-0.2668` n `8`; equity avg `-0.0146` n `140`; fx avg `-0.015` n `6`; index avg `-0.0036` n `26`; metal avg `-0.013` n `20`; unknown avg `-0.1633` n `946`
- 1h: commodity avg `0.0712` n `12`; crypto_alt avg `-0.2562` n `234`; crypto_major avg `-0.376` n `8`; equity avg `0.0379` n `140`; fx avg `0.0054` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0551` n `20`; unknown avg `90.5163` n `938`
- 4h: commodity avg `0.2264` n `12`; crypto_alt avg `-0.3268` n `234`; crypto_major avg `-0.5951` n `8`; equity avg `-0.339` n `140`; fx avg `-0.0089` n `6`; index avg `-0.0632` n `26`; metal avg `-0.226` n `20`; unknown avg `2.8413` n `937`
- 24h: commodity avg `0.7226` n `12`; crypto_alt avg `2.1607` n `234`; crypto_major avg `-0.4274` n `8`; equity avg `0.5842` n `140`; fx avg `-0.0167` n `6`; index avg `0.0175` n `26`; metal avg `-0.4268` n `20`; unknown avg `2.1949` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
