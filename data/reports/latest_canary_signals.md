# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T23:52:31.555660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `13`; crypto_alt avg `-0.0135` n `235`; crypto_major avg `-0.0254` n `8`; equity avg `-0.0004` n `150`; fx avg `0.0002` n `6`; index avg `0.008` n `26`; metal avg `-0.0207` n `20`; unknown avg `1.0718` n `1077`
- 1h: commodity avg `-0.031` n `13`; crypto_alt avg `0.3758` n `235`; crypto_major avg `0.2314` n `8`; equity avg `0.1138` n `150`; fx avg `0.0082` n `6`; index avg `0.024` n `26`; metal avg `0.0246` n `20`; unknown avg `1.0145` n `1075`
- 4h: commodity avg `0.1305` n `13`; crypto_alt avg `0.928` n `235`; crypto_major avg `0.2674` n `8`; equity avg `0.199` n `150`; fx avg `0.0246` n `6`; index avg `0.0442` n `26`; metal avg `0.061` n `20`; unknown avg `-0.2989` n `999`
- 24h: commodity avg `0.3842` n `13`; crypto_alt avg `-3.4473` n `235`; crypto_major avg `-3.2975` n `8`; equity avg `-1.258` n `150`; fx avg `-0.1511` n `6`; index avg `-0.1709` n `26`; metal avg `-0.6906` n `20`; unknown avg `247.925` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
