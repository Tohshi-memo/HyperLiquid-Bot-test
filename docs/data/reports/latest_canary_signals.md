# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T10:35:08.147555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.031` n `12`; crypto_alt avg `-0.0276` n `230`; crypto_major avg `-0.1431` n `8`; equity avg `-0.1478` n `113`; fx avg `0.006` n `6`; index avg `-0.0095` n `25`; metal avg `-0.0076` n `20`; unknown avg `0.0215` n `787`
- 1h: commodity avg `-0.0041` n `12`; crypto_alt avg `0.0452` n `230`; crypto_major avg `-0.1145` n `8`; equity avg `-0.0045` n `113`; fx avg `0.0193` n `6`; index avg `0.0141` n `25`; metal avg `0.0632` n `20`; unknown avg `0.025` n `787`
- 4h: commodity avg `-0.3292` n `12`; crypto_alt avg `0.019` n `230`; crypto_major avg `-0.3299` n `8`; equity avg `-0.4423` n `113`; fx avg `0.0326` n `6`; index avg `-0.025` n `25`; metal avg `0.026` n `20`; unknown avg `0.0251` n `787`
- 24h: commodity avg `-0.3159` n `12`; crypto_alt avg `-0.5567` n `230`; crypto_major avg `-0.5327` n `8`; equity avg `1.1682` n `113`; fx avg `0.0461` n `6`; index avg `0.1385` n `25`; metal avg `-0.5228` n `20`; unknown avg `0.1205` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2307`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
