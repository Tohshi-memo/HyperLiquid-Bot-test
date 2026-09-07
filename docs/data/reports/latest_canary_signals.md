# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T03:52:25.688104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0654` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0522` n `12`; crypto_alt avg `0.0559` n `232`; crypto_major avg `0.0038` n `8`; equity avg `0.0049` n `134`; fx avg `0.0053` n `6`; index avg `-0.005` n `26`; metal avg `-0.0247` n `20`; unknown avg `1.0818` n `794`
- 1h: commodity avg `0.0877` n `12`; crypto_alt avg `-0.9584` n `232`; crypto_major avg `-0.944` n `8`; equity avg `-0.0736` n `134`; fx avg `-0.0064` n `6`; index avg `-0.0214` n `26`; metal avg `-0.0969` n `20`; unknown avg `0.2916` n `792`
- 4h: commodity avg `0.069` n `12`; crypto_alt avg `-1.0431` n `232`; crypto_major avg `-1.0664` n `8`; equity avg `0.2476` n `134`; fx avg `-0.0253` n `6`; index avg `-0.001` n `26`; metal avg `-0.097` n `20`; unknown avg `134.1478` n `758`
- 24h: commodity avg `0.0613` n `12`; crypto_alt avg `-0.4239` n `232`; crypto_major avg `-0.9814` n `8`; equity avg `0.3374` n `134`; fx avg `0.0183` n `6`; index avg `-0.0076` n `26`; metal avg `-0.1857` n `20`; unknown avg `74.0518` n `650`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
