# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T01:07:27.447403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.7` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2706` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0832` n `13`; crypto_alt avg `-0.4343` n `239`; crypto_major avg `-0.3444` n `8`; equity avg `-0.8536` n `158`; fx avg `0.0049` n `6`; index avg `-0.1624` n `27`; metal avg `-0.0724` n `20`; unknown avg `0.47` n `1258`
- 1h: commodity avg `0.0848` n `13`; crypto_alt avg `-1.2636` n `239`; crypto_major avg `-1.0863` n `8`; equity avg `-1.7969` n `158`; fx avg `0.0037` n `6`; index avg `-0.307` n `27`; metal avg `-0.1878` n `20`; unknown avg `2.0114` n `1258`
- 4h: commodity avg `0.0289` n `13`; crypto_alt avg `-1.3014` n `239`; crypto_major avg `-1.5101` n `8`; equity avg `-1.3617` n `158`; fx avg `0.0399` n `6`; index avg `-0.2395` n `27`; metal avg `-0.0636` n `20`; unknown avg `168.7465` n `1195`
- 24h: commodity avg `0.2986` n `13`; crypto_alt avg `-0.2971` n `239`; crypto_major avg `-0.4554` n `8`; equity avg `-0.044` n `158`; fx avg `0.1644` n `6`; index avg `-0.1574` n `27`; metal avg `-0.583` n `20`; unknown avg `0.0477` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
