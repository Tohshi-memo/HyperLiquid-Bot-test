# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T05:37:27.975635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.87` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.055` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0101` n `13`; crypto_alt avg `-0.1545` n `237`; crypto_major avg `-0.0488` n `8`; equity avg `-0.0162` n `151`; fx avg `-0.0045` n `6`; index avg `-0.0133` n `26`; metal avg `0.0219` n `20`; unknown avg `0.5896` n `1199`
- 1h: commodity avg `0.1556` n `13`; crypto_alt avg `-0.3267` n `237`; crypto_major avg `-0.0684` n `8`; equity avg `-0.1245` n `151`; fx avg `-0.0043` n `6`; index avg `-0.0557` n `26`; metal avg `-0.0145` n `20`; unknown avg `0.3049` n `1197`
- 4h: commodity avg `0.1952` n `13`; crypto_alt avg `-2.0178` n `237`; crypto_major avg `-1.2828` n `8`; equity avg `-1.2021` n `151`; fx avg `-0.0657` n `6`; index avg `-0.2278` n `26`; metal avg `-0.2937` n `20`; unknown avg `6.6365` n `1175`
- 24h: commodity avg `-0.381` n `13`; crypto_alt avg `-0.9043` n `237`; crypto_major avg `-0.742` n `8`; equity avg `-2.2175` n `151`; fx avg `-0.026` n `6`; index avg `-0.3551` n `26`; metal avg `-0.5712` n `20`; unknown avg `119.1864` n `928`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
