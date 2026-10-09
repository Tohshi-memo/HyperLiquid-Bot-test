# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T06:52:26.089969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `13`; crypto_alt avg `0.0637` n `235`; crypto_major avg `0.0042` n `8`; equity avg `0.0026` n `150`; fx avg `-0.0106` n `6`; index avg `0.0034` n `26`; metal avg `0.0166` n `20`; unknown avg `2.0058` n `1078`
- 1h: commodity avg `0.0725` n `13`; crypto_alt avg `0.4066` n `235`; crypto_major avg `0.2333` n `8`; equity avg `0.1533` n `150`; fx avg `-0.0199` n `6`; index avg `0.0246` n `26`; metal avg `0.002` n `20`; unknown avg `0.8587` n `1046`
- 4h: commodity avg `-0.0209` n `13`; crypto_alt avg `1.0494` n `235`; crypto_major avg `0.3678` n `8`; equity avg `0.6329` n `150`; fx avg `0.0033` n `6`; index avg `0.0776` n `26`; metal avg `0.1131` n `20`; unknown avg `2.2851` n `1040`
- 24h: commodity avg `-0.0604` n `13`; crypto_alt avg `-0.9027` n `235`; crypto_major avg `-1.8539` n `8`; equity avg `-0.6609` n `150`; fx avg `0.1185` n `6`; index avg `0.0154` n `26`; metal avg `0.3903` n `20`; unknown avg `6.8344` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
