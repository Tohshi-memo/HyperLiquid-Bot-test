# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T07:22:33.293153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0003` n `13`; crypto_alt avg `-0.2039` n `235`; crypto_major avg `-0.0265` n `8`; equity avg `0.0086` n `143`; fx avg `-0.0019` n `6`; index avg `0.001` n `26`; metal avg `0.0014` n `20`; unknown avg `1.1352` n `984`
- 1h: commodity avg `0.0515` n `13`; crypto_alt avg `-0.2525` n `235`; crypto_major avg `-0.0714` n `8`; equity avg `0.0478` n `143`; fx avg `-0.0024` n `6`; index avg `0.0008` n `26`; metal avg `0.0005` n `20`; unknown avg `0.1027` n `982`
- 4h: commodity avg `-0.0392` n `13`; crypto_alt avg `-0.4451` n `235`; crypto_major avg `-0.1095` n `8`; equity avg `-0.0268` n `143`; fx avg `-0.0031` n `6`; index avg `-0.0114` n `26`; metal avg `0.0077` n `20`; unknown avg `-0.1498` n `954`
- 24h: commodity avg `0.2396` n `13`; crypto_alt avg `-1.7099` n `235`; crypto_major avg `-1.7718` n `8`; equity avg `0.4217` n `142`; fx avg `-0.0484` n `6`; index avg `0.2096` n `26`; metal avg `-0.3219` n `20`; unknown avg `-0.7972` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
