# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T10:37:31.245134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `0.0777` n `236`; crypto_major avg `0.0738` n `8`; equity avg `0.0099` n `151`; fx avg `0.0011` n `6`; index avg `-0.0061` n `26`; metal avg `0.0049` n `20`; unknown avg `1.1398` n `1193`
- 1h: commodity avg `0.0101` n `13`; crypto_alt avg `0.0343` n `236`; crypto_major avg `0.0087` n `8`; equity avg `0.0199` n `151`; fx avg `0.0176` n `6`; index avg `-0.014` n `26`; metal avg `-0.0031` n `20`; unknown avg `1.2463` n `1189`
- 4h: commodity avg `-0.1021` n `13`; crypto_alt avg `-0.4121` n `236`; crypto_major avg `-0.024` n `8`; equity avg `0.0005` n `151`; fx avg `0.0094` n `6`; index avg `0.0095` n `26`; metal avg `-0.0101` n `20`; unknown avg `0.0046` n `1171`
- 24h: commodity avg `0.3937` n `13`; crypto_alt avg `-2.274` n `236`; crypto_major avg `-1.3884` n `8`; equity avg `-3.5799` n `151`; fx avg `0.0111` n `6`; index avg `-0.5718` n `26`; metal avg `-0.2595` n `20`; unknown avg `8.6753` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1829`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1503`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1252`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0738`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
