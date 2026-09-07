# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T03:22:25.907872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.2054` n `232`; crypto_major avg `-0.1456` n `8`; equity avg `0.0053` n `134`; fx avg `0.0029` n `6`; index avg `0.0008` n `26`; metal avg `0.0094` n `20`; unknown avg `0.8243` n `794`
- 1h: commodity avg `-0.009` n `12`; crypto_alt avg `0.2076` n `232`; crypto_major avg `-0.1059` n `8`; equity avg `0.0825` n `134`; fx avg `0.0265` n `6`; index avg `-0.0406` n `26`; metal avg `-0.0061` n `20`; unknown avg `0.5799` n `764`
- 4h: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.5789` n `232`; crypto_major avg `-0.694` n `8`; equity avg `0.223` n `134`; fx avg `0.0109` n `6`; index avg `0.0058` n `26`; metal avg `-0.0648` n `20`; unknown avg `134.9471` n `756`
- 24h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.2234` n `232`; crypto_major avg `-0.2658` n `8`; equity avg `0.3554` n `134`; fx avg `0.0444` n `6`; index avg `-0.0223` n `26`; metal avg `-0.1273` n `20`; unknown avg `74.3345` n `650`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
