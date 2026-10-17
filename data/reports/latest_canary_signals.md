# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T17:52:26.957085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `13`; crypto_alt avg `0.0905` n `236`; crypto_major avg `0.1055` n `8`; equity avg `-0.0178` n `151`; fx avg `0.0016` n `6`; index avg `-0.0031` n `26`; metal avg `0.0022` n `20`; unknown avg `1.197` n `1193`
- 1h: commodity avg `0.0259` n `13`; crypto_alt avg `0.0188` n `236`; crypto_major avg `0.1212` n `8`; equity avg `-0.0502` n `151`; fx avg `-0.0029` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0049` n `20`; unknown avg `2.357` n `1167`
- 4h: commodity avg `0.0811` n `13`; crypto_alt avg `-0.8241` n `236`; crypto_major avg `-0.3863` n `8`; equity avg `-0.3065` n `151`; fx avg `-0.0269` n `6`; index avg `-0.0678` n `26`; metal avg `-0.0466` n `20`; unknown avg `2.3745` n `1135`
- 24h: commodity avg `0.1422` n `13`; crypto_alt avg `-1.8421` n `236`; crypto_major avg `-0.5104` n `8`; equity avg `-0.9782` n `151`; fx avg `-0.0142` n `6`; index avg `-0.1642` n `26`; metal avg `-0.0383` n `20`; unknown avg `3.6414` n `1027`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.171`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1477`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1132`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0718`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
