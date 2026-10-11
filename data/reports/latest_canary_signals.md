# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T16:37:27.274494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.1078` n `235`; crypto_major avg `0.1174` n `8`; equity avg `0.0509` n `150`; fx avg `-0.0002` n `6`; index avg `0.0055` n `26`; metal avg `0.01` n `20`; unknown avg `0.8429` n `1134`
- 1h: commodity avg `0.0219` n `13`; crypto_alt avg `0.7095` n `235`; crypto_major avg `0.8892` n `8`; equity avg `0.1681` n `150`; fx avg `-0.0022` n `6`; index avg `0.0213` n `26`; metal avg `0.0236` n `20`; unknown avg `1.8459` n `1110`
- 4h: commodity avg `-0.0656` n `13`; crypto_alt avg `1.982` n `235`; crypto_major avg `1.4058` n `8`; equity avg `0.2259` n `150`; fx avg `-0.0019` n `6`; index avg `0.0313` n `26`; metal avg `0.0319` n `20`; unknown avg `23.5826` n `1037`
- 24h: commodity avg `0.2602` n `13`; crypto_alt avg `2.1859` n `235`; crypto_major avg `1.0655` n `8`; equity avg `0.2724` n `150`; fx avg `0.0103` n `6`; index avg `0.0139` n `26`; metal avg `0.0536` n `20`; unknown avg `1.5381` n `925`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
