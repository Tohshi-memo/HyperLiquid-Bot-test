# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T05:52:28.081356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0438` n `12`; crypto_alt avg `-0.172` n `234`; crypto_major avg `-0.0444` n `8`; equity avg `-0.088` n `141`; fx avg `0.0049` n `6`; index avg `-0.0194` n `26`; metal avg `-0.0195` n `20`; unknown avg `34.9683` n `945`
- 1h: commodity avg `0.1473` n `12`; crypto_alt avg `0.3751` n `234`; crypto_major avg `0.424` n `8`; equity avg `0.073` n `141`; fx avg `-0.0139` n `6`; index avg `-0.0162` n `26`; metal avg `-0.0021` n `20`; unknown avg `323.5767` n `943`
- 4h: commodity avg `0.1134` n `12`; crypto_alt avg `1.4946` n `234`; crypto_major avg `0.5318` n `8`; equity avg `-0.2133` n `141`; fx avg `0.006` n `6`; index avg `-0.0467` n `26`; metal avg `0.0219` n `20`; unknown avg `1.8049` n `937`
- 24h: commodity avg `0.6389` n `12`; crypto_alt avg `-3.6505` n `234`; crypto_major avg `-3.669` n `8`; equity avg `-1.8262` n `140`; fx avg `0.0661` n `6`; index avg `-0.3839` n `26`; metal avg `-0.557` n `20`; unknown avg `585.2299` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
