# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T05:07:33.264849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `13`; crypto_alt avg `0.1428` n `235`; crypto_major avg `0.0997` n `8`; equity avg `0.1573` n `150`; fx avg `-0.0013` n `6`; index avg `0.0141` n `26`; metal avg `0.057` n `20`; unknown avg `-0.0055` n `1076`
- 1h: commodity avg `-0.0088` n `13`; crypto_alt avg `0.0815` n `235`; crypto_major avg `-0.1161` n `8`; equity avg `0.0755` n `150`; fx avg `0.0019` n `6`; index avg `0.0133` n `26`; metal avg `0.0315` n `20`; unknown avg `1.1332` n `1074`
- 4h: commodity avg `-0.2135` n `13`; crypto_alt avg `1.5037` n `235`; crypto_major avg `0.7434` n `8`; equity avg `0.6493` n `150`; fx avg `-0.008` n `6`; index avg `0.1081` n `26`; metal avg `0.2641` n `20`; unknown avg `1.0373` n `1068`
- 24h: commodity avg `0.0794` n `13`; crypto_alt avg `-1.2194` n `235`; crypto_major avg `-2.0724` n `8`; equity avg `-1.7009` n `150`; fx avg `0.1066` n `6`; index avg `-0.1789` n `26`; metal avg `0.1734` n `20`; unknown avg `5.7238` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
