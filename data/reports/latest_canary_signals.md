# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T08:37:27.825009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7321` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `0.4802` n `234`; crypto_major avg `0.6563` n `8`; equity avg `0.1568` n `140`; fx avg `-0.026` n `6`; index avg `0.0135` n `26`; metal avg `-0.0091` n `20`; unknown avg `4.5186` n `944`
- 1h: commodity avg `0.0078` n `12`; crypto_alt avg `0.9763` n `234`; crypto_major avg `1.3965` n `8`; equity avg `0.4256` n `140`; fx avg `-0.0601` n `6`; index avg `0.0577` n `26`; metal avg `0.0559` n `20`; unknown avg `21.2414` n `936`
- 4h: commodity avg `-0.0275` n `12`; crypto_alt avg `0.9995` n `234`; crypto_major avg `1.7288` n `8`; equity avg `0.6975` n `140`; fx avg `-0.1101` n `6`; index avg `0.1117` n `26`; metal avg `-0.0033` n `20`; unknown avg `4.2482` n `890`
- 24h: commodity avg `-0.6475` n `12`; crypto_alt avg `5.1969` n `234`; crypto_major avg `4.3764` n `8`; equity avg `1.8134` n `140`; fx avg `-0.1136` n `6`; index avg `0.3509` n `26`; metal avg `0.0332` n `20`; unknown avg `12.1593` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
