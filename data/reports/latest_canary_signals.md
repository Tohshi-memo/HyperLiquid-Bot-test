# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T11:52:30.064248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `13`; crypto_alt avg `0.1146` n `239`; crypto_major avg `0.0686` n `8`; equity avg `0.1458` n `162`; fx avg `0.0105` n `6`; index avg `0.0076` n `27`; metal avg `0.0293` n `20`; unknown avg `0.0948` n `1266`
- 1h: commodity avg `0.0364` n `13`; crypto_alt avg `1.1851` n `239`; crypto_major avg `1.0586` n `8`; equity avg `1.642` n `162`; fx avg `0.0225` n `6`; index avg `0.1391` n `27`; metal avg `0.1213` n `20`; unknown avg `159.8605` n `1264`
- 4h: commodity avg `0.2045` n `13`; crypto_alt avg `0.332` n `239`; crypto_major avg `0.1552` n `8`; equity avg `0.6311` n `162`; fx avg `-0.0376` n `6`; index avg `0.0727` n `27`; metal avg `0.016` n `20`; unknown avg `202.2179` n `1238`
- 24h: commodity avg `-0.613` n `13`; crypto_alt avg `1.182` n `239`; crypto_major avg `1.1848` n `8`; equity avg `-1.5808` n `162`; fx avg `-0.045` n `6`; index avg `-0.1615` n `27`; metal avg `-0.1702` n `20`; unknown avg `31.3606` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
