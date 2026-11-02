# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T16:07:35.013925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `13`; crypto_alt avg `-0.1173` n `239`; crypto_major avg `-0.1234` n `8`; equity avg `-0.1099` n `156`; fx avg `-0.0141` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0061` n `20`; unknown avg `0.2793` n `1253`
- 1h: commodity avg `0.0329` n `13`; crypto_alt avg `-0.1939` n `239`; crypto_major avg `-0.3512` n `8`; equity avg `0.0239` n `156`; fx avg `-0.0092` n `6`; index avg `0.0201` n `27`; metal avg `0.0485` n `20`; unknown avg `15.4053` n `1251`
- 4h: commodity avg `-0.4375` n `13`; crypto_alt avg `-0.2807` n `238`; crypto_major avg `-0.3752` n `8`; equity avg `-1.0505` n `156`; fx avg `-0.0033` n `6`; index avg `0.0294` n `27`; metal avg `0.3797` n `20`; unknown avg `18.7343` n `1253`
- 24h: commodity avg `-0.8943` n `13`; crypto_alt avg `-2.0269` n `238`; crypto_major avg `-0.7916` n `8`; equity avg `-0.3645` n `156`; fx avg `0.2693` n `6`; index avg `0.2661` n `27`; metal avg `0.3843` n `20`; unknown avg `7.6138` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
