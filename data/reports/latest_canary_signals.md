# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T03:52:28.953014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0467` n `12`; crypto_alt avg `0.33` n `234`; crypto_major avg `-0.0186` n `8`; equity avg `0.0627` n `140`; fx avg `0.0049` n `6`; index avg `0.0099` n `26`; metal avg `-0.0143` n `20`; unknown avg `0.801` n `944`
- 1h: commodity avg `0.0467` n `12`; crypto_alt avg `1.1199` n `234`; crypto_major avg `0.1913` n `8`; equity avg `0.0791` n `140`; fx avg `-0.0053` n `6`; index avg `0.0198` n `26`; metal avg `-0.0045` n `20`; unknown avg `-0.0249` n `942`
- 4h: commodity avg `-0.3465` n `12`; crypto_alt avg `1.105` n `234`; crypto_major avg `0.4155` n `8`; equity avg `0.3664` n `140`; fx avg `-0.0692` n `6`; index avg `0.0796` n `26`; metal avg `-0.0012` n `20`; unknown avg `16.8209` n `935`
- 24h: commodity avg `-0.6224` n `12`; crypto_alt avg `3.5152` n `234`; crypto_major avg `2.4875` n `8`; equity avg `1.0977` n `140`; fx avg `-0.0285` n `6`; index avg `0.2114` n `26`; metal avg `0.0366` n `20`; unknown avg `3.7247` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
