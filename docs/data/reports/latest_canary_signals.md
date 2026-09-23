# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T05:37:26.629021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0631` n `12`; crypto_alt avg `0.0719` n `234`; crypto_major avg `-0.0072` n `8`; equity avg `-0.0479` n `140`; fx avg `0.0206` n `6`; index avg `0.0016` n `26`; metal avg `-0.0427` n `20`; unknown avg `-0.2194` n `945`
- 1h: commodity avg `0.0714` n `12`; crypto_alt avg `0.0677` n `234`; crypto_major avg `-0.626` n `8`; equity avg `-0.2009` n `140`; fx avg `0.0485` n `6`; index avg `-0.0169` n `26`; metal avg `-0.0924` n `20`; unknown avg `0.8346` n `943`
- 4h: commodity avg `-0.0937` n `12`; crypto_alt avg `1.0292` n `234`; crypto_major avg `0.6711` n `8`; equity avg `-0.0894` n `140`; fx avg `0.0482` n `6`; index avg `0.0025` n `26`; metal avg `-0.1382` n `20`; unknown avg `-0.3827` n `937`
- 24h: commodity avg `-0.1338` n `12`; crypto_alt avg `4.7625` n `234`; crypto_major avg `2.6989` n `8`; equity avg `1.3132` n `140`; fx avg `-0.1613` n `6`; index avg `0.1246` n `26`; metal avg `0.2364` n `20`; unknown avg `2.6974` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
