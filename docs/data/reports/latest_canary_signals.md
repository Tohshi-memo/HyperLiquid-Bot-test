# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T03:22:27.726608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.67` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.6881` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.1854` n `237`; crypto_major avg `-0.1001` n `8`; equity avg `0.0431` n `151`; fx avg `-0.0055` n `6`; index avg `0.0195` n `26`; metal avg `-0.0288` n `20`; unknown avg `0.3778` n `1197`
- 1h: commodity avg `0.0422` n `13`; crypto_alt avg `-0.152` n `237`; crypto_major avg `-0.184` n `8`; equity avg `-0.0068` n `151`; fx avg `0.0033` n `6`; index avg `0.017` n `26`; metal avg `-0.0523` n `20`; unknown avg `-0.317` n `1191`
- 4h: commodity avg `0.136` n `13`; crypto_alt avg `-1.9272` n `237`; crypto_major avg `-1.7938` n `8`; equity avg `-1.0882` n `151`; fx avg `-0.0389` n `6`; index avg `-0.1057` n `26`; metal avg `-0.397` n `20`; unknown avg `10.0152` n `1185`
- 24h: commodity avg `-0.6084` n `13`; crypto_alt avg `-0.3994` n `237`; crypto_major avg `-0.5967` n `8`; equity avg `-1.8505` n `151`; fx avg `-0.0482` n `6`; index avg `-0.2402` n `26`; metal avg `-0.4525` n `20`; unknown avg `118.8585` n `938`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
