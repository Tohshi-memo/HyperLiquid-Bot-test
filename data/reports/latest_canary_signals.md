# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T10:07:25.966032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0855` n `12`; crypto_alt avg `0.0291` n `232`; crypto_major avg `0.0526` n `8`; equity avg `-0.0345` n `133`; fx avg `0.0036` n `6`; index avg `-0.0148` n `26`; metal avg `-0.0099` n `20`; unknown avg `0.0166` n `790`
- 1h: commodity avg `0.1272` n `12`; crypto_alt avg `-0.0626` n `232`; crypto_major avg `-0.2049` n `8`; equity avg `-0.2617` n `133`; fx avg `-0.045` n `6`; index avg `-0.0679` n `26`; metal avg `-0.1139` n `20`; unknown avg `0.6409` n `790`
- 4h: commodity avg `0.3669` n `12`; crypto_alt avg `0.2487` n `232`; crypto_major avg `0.0528` n `8`; equity avg `-0.2448` n `133`; fx avg `-0.0851` n `6`; index avg `-0.0988` n `26`; metal avg `-0.0365` n `20`; unknown avg `0.0003` n `788`
- 24h: commodity avg `0.4112` n `12`; crypto_alt avg `1.9313` n `232`; crypto_major avg `1.8122` n `8`; equity avg `1.6851` n `133`; fx avg `-0.4179` n `6`; index avg `0.1662` n `26`; metal avg `0.8748` n `20`; unknown avg `-0.1811` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0424`, n `668`, weak_sample_signal
