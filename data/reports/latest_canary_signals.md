# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T11:07:36.633739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4341` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `0.216` n `228`; crypto_major avg `0.2129` n `8`; equity avg `0.2929` n `86`; fx avg `-0.008` n `6`; index avg `0.0196` n `23`; metal avg `-0.0645` n `20`; unknown avg `0.0487` n `764`
- 1h: commodity avg `0.0755` n `12`; crypto_alt avg `-0.2002` n `228`; crypto_major avg `-0.1259` n `8`; equity avg `-0.136` n `86`; fx avg `0.0011` n `6`; index avg `-0.066` n `23`; metal avg `-0.1686` n `20`; unknown avg `-0.1445` n `764`
- 4h: commodity avg `0.1146` n `12`; crypto_alt avg `-1.0497` n `228`; crypto_major avg `-1.522` n `8`; equity avg `-0.271` n `86`; fx avg `-0.0693` n `6`; index avg `-0.0879` n `23`; metal avg `-0.0567` n `20`; unknown avg `-0.5023` n `620`
- 24h: commodity avg `-0.4744` n `12`; crypto_alt avg `-4.1706` n `228`; crypto_major avg `-4.3379` n `8`; equity avg `-4.4432` n `85`; fx avg `-0.1197` n `6`; index avg `-0.9262` n `23`; metal avg `-1.4155` n `20`; unknown avg `0.1759` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
