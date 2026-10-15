# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T05:37:27.715760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.4093` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0279` n `13`; crypto_alt avg `-0.1701` n `236`; crypto_major avg `-0.0638` n `8`; equity avg `-0.1964` n `151`; fx avg `0.0178` n `6`; index avg `-0.0705` n `26`; metal avg `-0.0277` n `20`; unknown avg `-0.1516` n `1136`
- 1h: commodity avg `0.0674` n `13`; crypto_alt avg `-1.1405` n `236`; crypto_major avg `-0.8166` n `8`; equity avg `-0.3999` n `151`; fx avg `0.0288` n `6`; index avg `-0.0914` n `26`; metal avg `-0.0528` n `20`; unknown avg `1.0568` n `1134`
- 4h: commodity avg `-0.0729` n `13`; crypto_alt avg `-2.813` n `236`; crypto_major avg `-1.5152` n `8`; equity avg `-0.5607` n `151`; fx avg `-0.0146` n `6`; index avg `-0.1059` n `26`; metal avg `-0.138` n `20`; unknown avg `0.9711` n `1128`
- 24h: commodity avg `-0.3462` n `13`; crypto_alt avg `-5.1895` n `236`; crypto_major avg `-3.6372` n `8`; equity avg `-5.7848` n `151`; fx avg `0.081` n `6`; index avg `-0.9985` n `26`; metal avg `-0.7726` n `20`; unknown avg `1392.8161` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1102`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1005`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0926`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0882`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.072`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0658`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
