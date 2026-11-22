# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T06:07:27.010532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.57` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_index_leads_crypto: score `1.3405` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `0.079` n `239`; crypto_major avg `0.2321` n `8`; equity avg `0.0073` n `166`; fx avg `-0.0041` n `6`; index avg `-0.0007` n `27`; metal avg `0.0151` n `20`; unknown avg `161.7904` n `1235`
- 1h: commodity avg `-0.0018` n `13`; crypto_alt avg `0.1202` n `239`; crypto_major avg `-0.0043` n `8`; equity avg `0.0559` n `166`; fx avg `0.0045` n `6`; index avg `0.0017` n `27`; metal avg `0.0324` n `20`; unknown avg `163.1308` n `1235`
- 4h: commodity avg `-0.0875` n `13`; crypto_alt avg `-0.7856` n `239`; crypto_major avg `-1.4424` n `8`; equity avg `-0.498` n `166`; fx avg `0.0057` n `6`; index avg `-0.1019` n `27`; metal avg `-0.1054` n `20`; unknown avg `2.4987` n `1227`
- 24h: commodity avg `-0.0283` n `13`; crypto_alt avg `3.5608` n `239`; crypto_major avg `5.2173` n `8`; equity avg `1.5422` n `166`; fx avg `-0.0217` n `6`; index avg `0.1752` n `27`; metal avg `0.1946` n `20`; unknown avg `607.696` n `1074`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
