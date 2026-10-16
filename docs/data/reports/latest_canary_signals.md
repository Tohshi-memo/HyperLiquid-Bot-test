# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T23:07:33.649323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0302` n `13`; crypto_alt avg `0.0036` n `236`; crypto_major avg `0.0126` n `8`; equity avg `-0.1198` n `151`; fx avg `0.0075` n `6`; index avg `-0.0105` n `26`; metal avg `-0.0104` n `20`; unknown avg `-0.0828` n `1191`
- 1h: commodity avg `-0.0035` n `13`; crypto_alt avg `0.1139` n `236`; crypto_major avg `0.0552` n `8`; equity avg `-0.2075` n `151`; fx avg `0.0044` n `6`; index avg `-0.0027` n `26`; metal avg `-0.0134` n `20`; unknown avg `1.4609` n `1189`
- 4h: commodity avg `0.0048` n `13`; crypto_alt avg `1.2988` n `236`; crypto_major avg `1.1948` n `8`; equity avg `-0.0532` n `151`; fx avg `0.0149` n `6`; index avg `0.0325` n `26`; metal avg `0.0648` n `20`; unknown avg `0.9461` n `1107`
- 24h: commodity avg `0.4455` n `13`; crypto_alt avg `-1.1317` n `236`; crypto_major avg `-0.9819` n `8`; equity avg `-4.0918` n `151`; fx avg `0.0288` n `6`; index avg `-0.6349` n `26`; metal avg `-0.0727` n `20`; unknown avg `39.7123` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1654`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0765`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0716`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0707`, n `666`, weak_sample_signal
