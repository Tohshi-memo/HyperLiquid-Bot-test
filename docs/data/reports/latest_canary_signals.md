# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T05:52:29.053447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1777` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0213` n `13`; crypto_alt avg `0.0912` n `235`; crypto_major avg `0.1409` n `8`; equity avg `0.0443` n `150`; fx avg `0.0029` n `6`; index avg `0.0029` n `26`; metal avg `0.0133` n `20`; unknown avg `0.2233` n `1076`
- 1h: commodity avg `-0.0038` n `13`; crypto_alt avg `0.5649` n `235`; crypto_major avg `0.4636` n `8`; equity avg `0.0377` n `150`; fx avg `-0.0044` n `6`; index avg `0.0023` n `26`; metal avg `-0.0304` n `20`; unknown avg `0.6462` n `1074`
- 4h: commodity avg `0.0296` n `13`; crypto_alt avg `-2.075` n `235`; crypto_major avg `-1.2135` n `8`; equity avg `-0.1935` n `150`; fx avg `-0.0362` n `6`; index avg `-0.0358` n `26`; metal avg `-0.1256` n `20`; unknown avg `1.5802` n `1068`
- 24h: commodity avg `0.4703` n `13`; crypto_alt avg `-2.9986` n `235`; crypto_major avg `-1.9492` n `8`; equity avg `-0.0381` n `149`; fx avg `0.0492` n `6`; index avg `-0.0392` n `26`; metal avg `-0.0235` n `20`; unknown avg `871.0228` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
