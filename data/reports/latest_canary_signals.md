# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T07:07:29.115083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0631` n `13`; crypto_alt avg `-0.0395` n `235`; crypto_major avg `0.0456` n `8`; equity avg `-0.1602` n `150`; fx avg `-0.0188` n `6`; index avg `-0.0311` n `26`; metal avg `-0.0357` n `20`; unknown avg `0.1151` n `1075`
- 1h: commodity avg `0.2376` n `13`; crypto_alt avg `0.0297` n `235`; crypto_major avg `0.0009` n `8`; equity avg `-0.5452` n `150`; fx avg `0.0004` n `6`; index avg `-0.1215` n `26`; metal avg `-0.0389` n `20`; unknown avg `0.1344` n `1069`
- 4h: commodity avg `0.3297` n `13`; crypto_alt avg `-0.3752` n `235`; crypto_major avg `-0.4922` n `8`; equity avg `-1.0011` n `150`; fx avg `-0.0304` n `6`; index avg `-0.1964` n `26`; metal avg `-0.2073` n `20`; unknown avg `0.8867` n `1041`
- 24h: commodity avg `0.6778` n `13`; crypto_alt avg `-1.3209` n `235`; crypto_major avg `-2.3418` n `8`; equity avg `-2.1066` n `150`; fx avg `-0.1479` n `6`; index avg `-0.3662` n `26`; metal avg `-0.2507` n `20`; unknown avg `417.0272` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
