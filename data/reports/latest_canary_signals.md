# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T00:37:48.376403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `13`; crypto_alt avg `0.0793` n `235`; crypto_major avg `0.1035` n `8`; equity avg `0.0612` n `150`; fx avg `-0.0185` n `6`; index avg `0.023` n `26`; metal avg `-0.0228` n `20`; unknown avg `0.0013` n `1076`
- 1h: commodity avg `0.0436` n `13`; crypto_alt avg `-0.0633` n `235`; crypto_major avg `0.0648` n `8`; equity avg `0.2094` n `150`; fx avg `0.0064` n `6`; index avg `0.0532` n `26`; metal avg `-0.0385` n `20`; unknown avg `-0.0066` n `1068`
- 4h: commodity avg `0.0977` n `13`; crypto_alt avg `-0.1704` n `235`; crypto_major avg `-0.1237` n `8`; equity avg `0.2608` n `150`; fx avg `0.0195` n `6`; index avg `0.068` n `26`; metal avg `-0.0138` n `20`; unknown avg `-0.165` n `1046`
- 24h: commodity avg `0.386` n `13`; crypto_alt avg `-1.157` n `235`; crypto_major avg `-0.871` n `8`; equity avg `0.5035` n `149`; fx avg `0.1264` n `6`; index avg `0.0365` n `26`; metal avg `0.0282` n `20`; unknown avg `870.8924` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
