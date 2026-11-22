# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T03:52:23.456773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3155` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `0.0279` n `239`; crypto_major avg `0.0399` n `8`; equity avg `-0.038` n `166`; fx avg `0.002` n `6`; index avg `0.0069` n `27`; metal avg `-0.003` n `20`; unknown avg `1.0754` n `1263`
- 1h: commodity avg `-0.0435` n `13`; crypto_alt avg `-0.2588` n `239`; crypto_major avg `-0.525` n `8`; equity avg `-0.132` n `166`; fx avg `0.0084` n `6`; index avg `-0.0143` n `27`; metal avg `-0.0671` n `20`; unknown avg `1.7087` n `1261`
- 4h: commodity avg `-0.0908` n `13`; crypto_alt avg `-1.2143` n `239`; crypto_major avg `-1.3932` n `8`; equity avg `-0.4139` n `166`; fx avg `0.002` n `6`; index avg `-0.0777` n `27`; metal avg `-0.1331` n `20`; unknown avg `176.5353` n `1257`
- 24h: commodity avg `-0.0108` n `13`; crypto_alt avg `2.7042` n `239`; crypto_major avg `4.4383` n `8`; equity avg `1.4472` n `166`; fx avg `-0.0199` n `6`; index avg `0.2074` n `27`; metal avg `0.1609` n `20`; unknown avg `232.8795` n `1082`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
