# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T01:52:28.030107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `12`; crypto_alt avg `-0.1745` n `234`; crypto_major avg `-0.1145` n `8`; equity avg `-0.0145` n `140`; fx avg `-0.0135` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0486` n `20`; unknown avg `-0.0885` n `944`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `-0.7325` n `234`; crypto_major avg `-0.7948` n `8`; equity avg `-0.3112` n `140`; fx avg `0.0106` n `6`; index avg `-0.0296` n `26`; metal avg `-0.1073` n `20`; unknown avg `-0.3149` n `942`
- 4h: commodity avg `0.1762` n `12`; crypto_alt avg `0.5494` n `234`; crypto_major avg `-0.7118` n `8`; equity avg `0.2437` n `140`; fx avg `-0.1637` n `6`; index avg `0.0545` n `26`; metal avg `0.0329` n `20`; unknown avg `0.9848` n `936`
- 24h: commodity avg `-0.1566` n `12`; crypto_alt avg `4.1382` n `234`; crypto_major avg `4.7191` n `8`; equity avg `2.3178` n `140`; fx avg `-0.2544` n `6`; index avg `0.5015` n `26`; metal avg `-0.0792` n `20`; unknown avg `11.4921` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
