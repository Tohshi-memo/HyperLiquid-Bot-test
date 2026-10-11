# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T19:31:03.644464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `13`; crypto_alt avg `-0.0508` n `235`; crypto_major avg `-0.0634` n `8`; equity avg `0.0059` n `150`; fx avg `-0.0005` n `6`; index avg `0.0062` n `26`; metal avg `-0.0014` n `20`; unknown avg `6.4102` n `1134`
- 1h: commodity avg `0.0282` n `13`; crypto_alt avg `-0.0061` n `235`; crypto_major avg `-0.2136` n `8`; equity avg `-0.0194` n `150`; fx avg `-0.0047` n `6`; index avg `0.0002` n `26`; metal avg `0.0008` n `20`; unknown avg `-0.1476` n `1130`
- 4h: commodity avg `0.0688` n `13`; crypto_alt avg `0.6148` n `235`; crypto_major avg `0.5191` n `8`; equity avg `0.1715` n `150`; fx avg `0.0019` n `6`; index avg `0.0363` n `26`; metal avg `0.04` n `20`; unknown avg `0.0077` n `1092`
- 24h: commodity avg `0.2863` n `13`; crypto_alt avg `1.7828` n `235`; crypto_major avg `0.5517` n `8`; equity avg `0.2737` n `150`; fx avg `0.0188` n `6`; index avg `0.047` n `26`; metal avg `0.0727` n `20`; unknown avg `0.8111` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
