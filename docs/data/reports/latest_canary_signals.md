# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T00:37:26.718360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `13`; crypto_alt avg `0.1078` n `237`; crypto_major avg `-0.0383` n `8`; equity avg `0.0256` n `152`; fx avg `-0.0007` n `6`; index avg `-0.0015` n `26`; metal avg `0.0064` n `20`; unknown avg `-0.3092` n `1230`
- 1h: commodity avg `0.079` n `13`; crypto_alt avg `0.0273` n `237`; crypto_major avg `-0.2429` n `8`; equity avg `0.0178` n `152`; fx avg `-0.0063` n `6`; index avg `0.0023` n `26`; metal avg `-0.0145` n `20`; unknown avg `163.3802` n `1222`
- 4h: commodity avg `0.166` n `13`; crypto_alt avg `-1.1628` n `237`; crypto_major avg `-0.9756` n `8`; equity avg `-0.2668` n `152`; fx avg `0.0252` n `6`; index avg `-0.0438` n `26`; metal avg `-0.068` n `20`; unknown avg `0.1422` n `1200`
- 24h: commodity avg `0.6203` n `13`; crypto_alt avg `-1.0626` n `237`; crypto_major avg `-0.8076` n `8`; equity avg `1.1219` n `152`; fx avg `0.0114` n `6`; index avg `0.0967` n `26`; metal avg `-0.1484` n `20`; unknown avg `200.3867` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
