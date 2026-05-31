# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T17:22:18.908929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3973` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0378` n `12`; crypto_alt avg `0.1944` n `228`; crypto_major avg `0.096` n `8`; equity avg `0.0065` n `69`; fx avg `0.0` n `6`; index avg `0.0158` n `23`; metal avg `-0.0193` n `18`; unknown avg `-0.0393` n `421`
- 1h: commodity avg `-0.0302` n `12`; crypto_alt avg `-0.2781` n `228`; crypto_major avg `-0.3213` n `8`; equity avg `-0.0572` n `69`; fx avg `0.0075` n `6`; index avg `0.0668` n `23`; metal avg `0.0251` n `18`; unknown avg `0.3712` n `421`
- 4h: commodity avg `0.1209` n `12`; crypto_alt avg `-1.5661` n `228`; crypto_major avg `-1.1517` n `8`; equity avg `-0.0574` n `69`; fx avg `-0.0104` n `6`; index avg `0.2456` n `23`; metal avg `-0.058` n `18`; unknown avg `-0.2889` n `421`
- 24h: commodity avg `0.5877` n `12`; crypto_alt avg `-1.4852` n `228`; crypto_major avg `-0.5315` n `8`; equity avg `0.8313` n `69`; fx avg `-0.0116` n `6`; index avg `0.0753` n `23`; metal avg `-0.1354` n `18`; unknown avg `-0.0319` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
